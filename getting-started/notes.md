# Getting started: models, messages, and context

**Sources:** [classes 3–4](../sources/README.md#foundations) introduce LangChain as an orchestration layer; classes 5–7 cover chat messages and context.

## Why use LangChain?

An LLM application often needs a prompt, model call, conversation state, retrieved data, tools, and output processing. LangChain supplies components with compatible interfaces so the application can connect these steps. A basic model call alone does not create a lasting conversation.

## The first model call

`ChatOpenAI(...).invoke(...)` returns an `AIMessage` object. Read `response.content` for text, and inspect metadata only when needed. Keep the API key in `OPENAI_API_KEY`, never in the program.

Run [chat_model_call.py](programs/chat_model_call.py) to see the response object and text. It makes a live API call.

## Three common message roles

| Type | Purpose |
| --- | --- |
| `SystemMessage` | Sets behavior and context |
| `HumanMessage` | Carries a user's input |
| `AIMessage` | Carries the model's response |

Run [message_roles.py](programs/message_roles.py) to inspect these objects without an API call. Messages are ordered: changing their order can change the conversation's meaning.

## Context and stateless calls

Each model call uses the messages supplied for that call. To answer a follow-up, the application must include relevant prior messages. The later [conversation history guide](../conversation-history-and-memory/notes.md) shows how to do this safely.

## Source material

- [Class 3 PDF](../sources/pdfs/class3-langchain.pdf), [class 4 PDF](../sources/pdfs/class4-langchain.pdf)
- [Class 5 PDF](../sources/pdfs/class5-langchain.pdf), [class 6 PDF](../sources/pdfs/class6-langchain.pdf), [class 7 PDF](../sources/pdfs/class7-langchain.pdf)
