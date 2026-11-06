# Multi-user chatbots: classes 42–44

## Study path

Class 42 is a [25-question review](../sources/pdfs/Langchain%20-%20class42.pdf) of stateless model calls, manual history, session isolation and persistence. Use the earlier [conversation history guide](../conversation-history-and-memory/notes.md) and its [file history example](../conversation-history-and-memory/programs/file_chat_history.py) before attempting the larger applications.

Class 43 combines signup, login, multiple users, file-backed chat history, LCEL and `RunnableWithMessageHistory` in a [multi-user chatbot](../sources/pdfs/Langchain%20-%20class43.pdf). A user account and a conversation session are different identities: one account could have several conversations. Store each conversation under its own opaque ID, and check that one user cannot select another user's history. The [offline session isolation demo](programs/session_isolation.py) shows this boundary without calling an LLM.

Class 44 moves the same idea to [Supabase PostgreSQL with JSONB](../sources/pdfs/Langchain%20-%20class44.pdf). JSONB stores flexible message data within a relational database. LangChain messages must be serialized before storage and reconstructed when loaded. Database access control, password hashing, and credentials need a proper implementation before the classroom design is used with real accounts. The earlier [message serialization demo](../conversation-history-and-memory/programs/message_serialization.py) covers the data conversion.

## Review questions

1. Why does calling the same model object twice not automatically carry history into the second call?
2. What should identify an account, and what should identify one conversation?
3. How does a file-backed or database-backed history survive a Python restart?
4. Why is JSONB still part of PostgreSQL rather than a separate NoSQL database?

The original PDFs contain the full quiz and application walkthroughs. This guide is a study summary, not a deployed authentication service.
