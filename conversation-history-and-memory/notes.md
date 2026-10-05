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

## Source material

- [Classes 29–36](../sources/README.md#conversation-history-and-memory)
