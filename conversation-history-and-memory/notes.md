# Conversation history and memory

![Class 29 overview](../sources/images/class%2029.png)

## Keep the full conversation in the application

Model calls are stateless unless prior context is supplied. A manual chat loop keeps a list of messages: append the `HumanMessage`, call the model with the list, then append the returned `AIMessage`. Run [manual_chat_history.py](programs/manual_chat_history.py) for a live terminal chatbot.

## Limit context deliberately

![Class 32 overview](../sources/images/class%2032.png)

Long histories consume tokens, time, and money. A simple window keeps the most recent messages. Preserve the `SystemMessage` separately so slicing the conversation cannot remove it. [recent_history_window.py](programs/recent_history_window.py) demonstrates this without an API call. A window of six *messages* is usually three user/assistant turns, assuming each turn has exactly two messages.

For longer chats, a summary of older turns plus recent messages can keep more useful context. A summary may lose detail, so keep the complete transcript separately if an audit or later review is needed. Persist state per session or user when conversations must survive restarts; never mix histories between users.

## Legacy memory APIs

![Class 34 overview](../sources/images/class%2034.png)

Classes 33–36 explain `ConversationBufferMemory`, `ConversationBufferWindowMemory`, and `ConversationChain`. These appear in older tutorials and codebases. Their examples use the separate `langchain_classic` package and are preserved in the source PDFs. For new work, start with explicit history handling or a current message-history pattern; choose storage and session isolation deliberately.

## Session-based history with runnables (classes 37–38)

![Class 37 overview](../sources/images/class%2037.png)

`RunnableWithMessageHistory` wraps a model or LCEL chain. A history factory receives a `session_id` and returns that session's message store. The wrapper loads previous messages before each call, then saves the new human and AI messages. Reusing an ID continues that conversation; a different ID selects a separate history. A session ID identifies a **conversation**, which may differ from a user ID when one user has several chats.

The [offline session demo](programs/session_history.py) shows two independent conversations without an API key. Its in-memory dictionary is only for learning: it disappears when the process exits and is not shared across processes. Keep the complete transcript or use persistent storage when continuity matters.

![Class 38 overview](../sources/images/class%2038.png)

For an LCEL chain with dictionary input, `MessagesPlaceholder("history")` marks where previous messages enter the prompt. `input_messages_key="question"` names the current user message, and `history_messages_key="history"` must match the placeholder. Pass the session in `config={"configurable": {"session_id": session_id}}` on **every** invocation. The [multi-user CLI example](programs/multi_user_chat.py) demonstrates this with a chat model and requires an API key. Use a unique, opaque ID for each conversation; do not assume a display name is unique.

The class notes also discuss legacy `save_context()`, `load_memory_variables()`, and `clear()` methods. Those belong to the older memory classes above, not to `RunnableWithMessageHistory`. A valid history wrapper still needs appropriate storage, context limits, and testing of session isolation. The wrapper may emit a deprecation warning in the pinned `langchain-core` version; keep this example for understanding the class material. For a new LangChain agent, the current [short-term memory guide](https://docs.langchain.com/oss/python/langchain/short-term-memory) describes checkpoint-based memory; the [RunnableWithMessageHistory reference](https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory) documents this LCEL pattern.

## Save message objects as JSON (October 6 lesson)

LangChain messages are Python objects. `message_to_dict()` converts one message to a storable dictionary; `messages_from_dict()` reconstructs a sequence of messages. `json.dumps()` and `json.loads()` convert between Python data and JSON text. Run [message_serialization.py](programs/message_serialization.py) offline to see a complete round trip. Serialization by itself does not save anything after the process stops; a file or database must hold the JSON.

## Persistent chat sessions (October 7–8 lessons)

[file_chat_history.py](programs/file_chat_history.py) implements `BaseChatMessageHistory` with `messages`, `add_messages()`, and `clear()`. It stores one JSON file per session. The offline demo reopens a session to prove that messages survive creation of a new history object. [persistent_chatbot.py](programs/persistent_chatbot.py) connects this store to `RunnableWithMessageHistory` and a live model, so the same conversation ID can continue after Python restarts.

The file store uses a hash of the conversation ID as its filename and replaces files after writing. It is a teaching example for a single process; concurrent writers need a transactional database or suitable locking. The `chat_history/` directory is ignored by Git because it can contain private conversations. Do not publish it with the study notes.

The original class 34–36 buffer and window examples are available as [legacy_memory_examples.py](programs/legacy_memory_examples.py); [legacy_conversation_chain.py](programs/legacy_conversation_chain.py) shows the older automated chat loop. They need `langchain-classic` in a separate compatible environment and are kept for reading older code rather than as the current default. The later serialization and persistence material was supplied through the [ChatGPT project lessons](../lessons/README.md), without local source PDFs or images.

## Source material

- [Classes 29–38](../sources/README.md#conversation-history-and-memory)
