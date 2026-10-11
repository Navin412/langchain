# Class 43 — Multi-user chatbot with persistent history

![Class 43 infographic](../sources/images/class%2043.png)

The [original class 43 PDF](../sources/pdfs/Langchain%20-%20class43.pdf) explains a signup and login menu, a user registry in `users.json`, and a separate JSON conversation history for each account. The infographic above summarizes the lesson architecture.

## How the classroom example works

1. Signup collects a name, username, and password; login selects the current user.
2. The username is passed as the `session_id` to `RunnableWithMessageHistory`.
3. `FileChatMessageHistory` loads that session's messages from JSON.
4. `MessagesPlaceholder("history")` inserts earlier messages before the new question.
5. After the model responds, the wrapper appends the new user and AI messages to the selected history.

The classroom design assigns one conversation to each username. A product that allows several chats per account should use a separate conversation ID and check that the signed-in user owns that conversation.

## Try the reviewed building blocks

- [File-backed history](../conversation-history-and-memory/programs/file_chat_history.py) demonstrates saving, reopening, and clearing a session without an API key. It hashes the session ID before making a filename and writes through a temporary file.
- [Persistent chatbot](../conversation-history-and-memory/programs/persistent_chatbot.py) connects the file store to an LCEL prompt and a live model. It requires `OPENAI_API_KEY`.
- [Multi-user session demo](../conversation-history-and-memory/programs/multi_user_chat.py) shows separate in-memory sessions, but does not include account login or persistence.

## Important limits in the source example

The PDF stores passwords directly in `users.json` and compares them as plain text. Do not reuse that account code for real users. A real application needs a password hashing library, access controls for account and chat files, and a storage design that handles concurrent writes. The infographic also labels the design “production ready”; treat that as a classroom claim rather than a verified security assessment.

The repository's file store is an educational, single-process example. Its hashed filename prevents session IDs from becoming file paths; it is not encryption or authentication. The `chat_history/` directory is ignored by Git so locally generated conversations are not published.
