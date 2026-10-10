# October 8, 2026 — LangChain Persistent Chat History Using JSON Files

## Learning objectives

Understand how to store and retrieve conversation history across application restarts using `BaseChatMessageHistory`, JSON files, message serialization, session IDs, and `RunnableWithMessageHistory`.

## 1. Main concept: persistent conversation history

An in-memory chatbot loses its history when the Python process stops. Persistent history saves messages to durable storage and reloads them in future runs.

```text
User enters session_id
          ↓
get_session_history(session_id)
          ↓
FileChatMessageHistory
          ↓
Load chat_history/<session_id>.json
          ↓
Deserialize JSON into LangChain Messages
          ↓
System Prompt + Previous History + New Question
          ↓
ChatOpenAI
          ↓
Answer + Updated Messages
          ↓
Serialize and save to the same JSON file
```

**Example:** `session_id="durga"` stores history in `chat_history/durga.json`; `session_id="ravi"` uses `chat_history/ravi.json`. Entering the same session ID after restarting the script retrieves earlier saved messages.

## 2. Important components

| Component | Purpose |
|---|---|
| `BaseChatMessageHistory` | Base interface for custom message-history storage |
| `messages` | Loads saved messages for the selected session |
| `add_messages()` | Appends new messages and persists them |
| `clear()` | Erases saved conversation history for that session |
| `message_to_dict()` | Serializes a LangChain message into a dictionary |
| `messages_from_dict()` | Recreates LangChain message objects from dictionaries |
| `MessagesPlaceholder("history")` | Inserts previous turns into the prompt |
| `RunnableWithMessageHistory` | Automatically retrieves and updates chat history |
| `session_id` | Selects which session's JSON file to access |

## 3. Full original Python program

The following code is preserved as supplied for study reference.

```python
import os
import json

from langchain_openai import ChatOpenAI

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.chat_history import (
    BaseChatMessageHistory
)

from langchain_core.messages import (
    BaseMessage,
    message_to_dict,
    messages_from_dict
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)


# ========================================
# 1. PERSISTENT CHAT HISTORY
# ========================================

class FileChatMessageHistory(
    BaseChatMessageHistory
):

    def __init__(
        self,
        session_id,
        storage_path="chat_history"
    ):

        self.session_id = session_id

        os.makedirs(
            storage_path,
            exist_ok=True
        )

        self.file_path = os.path.join(
            storage_path,
            f"{session_id}.json"
        )


    # ------------------------------------
    # LOAD MESSAGES
    # ------------------------------------

    @property
    def messages(self):

        if not os.path.exists(
            self.file_path
        ):
            return []

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return messages_from_dict(
            data
        )

    # ------------------------------------
    # SAVE MESSAGES
    # ------------------------------------

    def add_messages(
        self,
        messages: list[BaseMessage]
    ) -> None:

        all_messages = list(
            self.messages
        )

        all_messages.extend(
            messages
        )

        serialized = [
            message_to_dict(message)
            for message in all_messages
        ]

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                serialized,
                file,
                ensure_ascii=False,
                indent=2
            )


    # ------------------------------------
    # CLEAR HISTORY
    # ------------------------------------

    def clear(self) -> None:

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file
            )


# ========================================
# 2. CREATE MODEL
# ========================================

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ========================================
# 3. CREATE PROMPT
# ========================================

prompt = ChatPromptTemplate.from_messages(

    [
        (
            "system",
            """
            You are a helpful AI assistant.
            Answer in simple English.
            """
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),

        (
            "human",
            "{question}"
        )
    ]
)


# ========================================
# 4. CREATE LCEL CHAIN
# ========================================

chain = (
    prompt
    | llm
)

# ========================================
# 5. GET SESSION HISTORY
# ========================================

def get_session_history(
    session_id
):

    return FileChatMessageHistory(
        session_id
    )


# ========================================
# 6. ADD MESSAGE HISTORY
# ========================================

chatbot = RunnableWithMessageHistory(

    chain,
    get_session_history,

    input_messages_key="question",

    history_messages_key="history"
)


# ========================================
# 7. GET SESSION ID
# ========================================

session_id = input(
    "Enter session id: "
)


print("\nAI Chatbot")
print("Type 'exit' to stop")
print("------------------------")
# ========================================
# 8. CHAT LOOP
# ========================================

while True:

    user_input = input(
        "\nYou: "
    )


    if user_input.lower() == "exit":

        print(
            "Chat ended."
        )

        break


    response = chatbot.invoke(

        {
            "question": user_input
        },

        config={
            "configurable": {
                "session_id":
                session_id
            }
        }
    )


    print(
        "AI:",
        response.content
    )
```

## 4. Step-by-step explanation

### Step 1 — Create file-based history

`FileChatMessageHistory` extends `BaseChatMessageHistory`. Its constructor creates the target directory if necessary and generates the path `chat_history/<session_id>.json`.

### Step 2 — Load messages

The `messages` property returns an empty list if the session file does not yet exist. Otherwise, `json.load()` reads dictionaries from disk and `messages_from_dict()` reconstructs LangChain messages.

### Step 3 — Save messages

`add_messages()` reads the existing messages, appends the newly received messages, converts each message using `message_to_dict()`, and writes the list as formatted JSON.

### Step 4 — Clear messages

`clear()` overwrites the current session file with an empty JSON array (`[]`). It clears only that session's history.

### Step 5 — Model and prompt

`ChatOpenAI` supplies the language model. The prompt contains a system instruction, `MessagesPlaceholder("history")`, and the new user question `{question}`.

### Step 6 — Build the LCEL chain

`prompt | llm` means the prompt output is passed to the model.

### Step 7 — Wrap with history management

`RunnableWithMessageHistory(chain, get_session_history, input_messages_key="question", history_messages_key="history")` coordinates history loading and saving. The `session_id` in `config["configurable"]` tells the wrapper which file-backed history to use.

### Step 8 — Interactive loop

The chatbot keeps receiving a question, invoking the same session-specific chain, printing the response, and saving turns, until the user types `exit`.

## 5. Sample workflow (illustrative)

```text
Run 1 — Enter session id: durga
You: My favorite language is Python.
AI: ...
You: exit

Disk now contains: chat_history/durga.json

Run 2 — Enter session id: durga
You: What is my favorite language?
AI: Python.
```

The model's exact wording may vary, but prior conversation becomes available after restart.

## 6. In-memory vs persistent history

| Feature | In-memory | JSON file-based |
|---|---|---|
| Survives Python restart | No | Yes |
| Separate user sessions | Possible | Yes, via session files |
| Storage | Process RAM | Local disk |
| Appropriate scale | Small demos | Learning, prototypes, single-process apps |
| Multi-worker concurrency | Requires design | Needs locking or a transactional store |

## 7. Practical engineering notes

- **Model availability:** `gpt-5.6-luna` is preserved exactly as supplied; confirm that it is an actual supported API model in your account before execution, or substitute an available model ID.
- **Package requirements:** `pip install langchain-core langchain-openai` and set `OPENAI_API_KEY` in the environment.
- **Session security:** Never use an untrusted `session_id` directly in a file path in production; validate or transform it to avoid path traversal.
- **File integrity:** Concurrent writers can overwrite updates because `add_messages()` reads and rewrites the entire file. For production use, consider SQLite/PostgreSQL and transactions or locking.
- **Privacy:** JSON chat logs may contain private or sensitive content; apply suitable access control, retention policies, and encryption as needed.
- **Failure handling:** Production code should handle malformed JSON and I/O errors.
- **Efficiency:** The current design rewrites the entire conversation on each save; that is fine for a small educational example but less ideal for large histories.

## 8. Quick revision

1. **Persistence** means conversation history survives process restarts.
2. `messages` = **load**; `add_messages()` = **save**; `clear()` = **erase**.
3. `message_to_dict()` = **serialization**; `messages_from_dict()` = **deserialization**.
4. `MessagesPlaceholder("history")` injects previous messages into a prompt.
5. `session_id` chooses the correct conversation history.
6. `RunnableWithMessageHistory` automates reading and updating history around the chain.

## 9. Practice questions

1. Which method converts a LangChain message to a dictionary? **`message_to_dict()`**.
2. What is returned when the JSON file is absent? **An empty list**.
3. Which parameter specifies the prompt's existing-history field? **`history_messages_key="history"`**.
4. What happens if two different session IDs are used? **Two separate session JSON files are used**.
5. Why can this chatbot remember after restarting Python? **It reloads previous messages from persistent JSON storage**.

## 10. Visual Lesson Reference — Class 41, October 8, 2026

![AI with Durga Sir — LangChain Class 41: Persistent Chat History Using JSON Files](https://chatgpt.com/api/library/files/libfile_8c4329670db881919ae53285b997ada1/download)

This lesson infographic summarizes in-memory versus persistent history, the RunnableWithMessageHistory execution flow, the custom FileChatMessageHistory class, its core methods, BaseMessage type hints, the storage interface contract, and production considerations.

[Open original Class 41 infographic](https://chatgpt.com/api/library/files/libfile_8c4329670db881919ae53285b997ada1/download)

