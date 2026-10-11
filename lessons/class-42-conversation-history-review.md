# Class 42 — Conversation history and memory review

The [original class 42 PDF](../sources/pdfs/Langchain%20-%20class42.pdf) contains 25 multiple-choice questions with answers and explanations. Use it to check the concepts in the [conversation history guide](../conversation-history-and-memory/notes.md) and the linked programs.

## Review map

| Questions | Focus | Practice |
| --- | --- | --- |
| 1–7 | Stateless calls, manual message history, and recent-message windows | [Manual history](../conversation-history-and-memory/programs/manual_chat_history.py), [window](../conversation-history-and-memory/programs/recent_history_window.py) |
| 8–12 | Legacy buffer and `ConversationChain` APIs | [Legacy examples](../conversation-history-and-memory/programs/legacy_memory_examples.py) |
| 13–17 | `RunnableWithMessageHistory`, session IDs, and placeholders | [Session demo](../conversation-history-and-memory/programs/session_history.py) |
| 18–22 | Message serialization, JSON, and persistence | [Serialization](../conversation-history-and-memory/programs/message_serialization.py), [file store](../conversation-history-and-memory/programs/file_chat_history.py) |
| 23–25 | Session isolation and multi-user design | [Storage comparison](../conversation-history-and-memory/programs/storage_mode_comparison.py), [class 43](class-43-multi-user-persistent-chatbot.md) |

## Key distinctions

- Reusing a model object does not automatically include earlier messages. Supply the relevant history on each call.
- A window limits messages sent to the model; it need not delete the complete stored transcript. Three ordinary user/assistant turns are usually six messages.
- `session_id` selects a conversation. A user can have more than one conversation, so a user ID and a conversation ID need not be identical.
- `message_to_dict()` makes one LangChain message a Python dictionary. `json.dumps()` makes JSON text. Persistence requires writing that text to a file or other durable store.
- `RunnableWithMessageHistory` manages loading and updating messages, but the history factory determines where they live and whether they survive a restart.

## Answer key

| Questions | Answers |
| --- | --- |
| 1–5 | C, B, C, B, C |
| 6–10 | B, C, B, B, C |
| 11–15 | C, B, A, C, B |
| 16–20 | D, C, B, C, D |
| 21–25 | C, B, B, C, D |

Read the explanations in the PDF after attempting each question. The legacy APIs in questions 8–12 describe older LangChain lessons; the [memory guide](../conversation-history-and-memory/notes.md#legacy-memory-apis) explains where they fit today.
