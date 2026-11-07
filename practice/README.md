# Python practice by class

These are **runnable adaptations** of the exercises in the original class PDFs, with small sample inputs. They are not exact PDF transcriptions. The [PDF archive](../sources/README.md) remains the source for the instructor's complete code and explanations. Install the extra loader packages with `python -m pip install -r requirements-practice.txt` from the repository root.

For the original examples in searchable, copyable text, open the [page-by-page PDF text index](pdf-text/README.md). The text exports are references, not checked `.py` files.

Run an offline exercise from the repository root, for example:

```powershell
python practice/class49_text_loader.py
python practice/class52_csv_loader.py
python practice/class55_pdf_core.py "sources/pdfs/Langchain - class48.pdf"
```

To run the checked practice set in one step, use `python practice/run_all.py`. Add `--include-web` to run the two local web examples as well.

| Class | PDF topic | Practice files | Coverage |
| --- | --- | --- | --- |
| 3–7 | First model calls and messages | [Chat model](../getting-started/programs/chat_model_call.py), [message roles](../getting-started/programs/message_roles.py) | Selected exercises; a model call needs an API key. |
| 8–12 | Prompt templates and chat prompts | [Prompt template](../prompts-and-messages/programs/prompt_template.py), [defaults](../prompts-and-messages/programs/prompt_defaults.py), [chat prompt](../prompts-and-messages/programs/chat_prompt_template.py), [interview helper](../prompts-and-messages/programs/interview_helper.py) | Main patterns; individual PDF variants are not all separate files. |
| 13–18 | Parsing, Pydantic, structured output | [String parser](../output-parsers-and-structured-data/programs/string_output_parser.py), [Pydantic](../output-parsers-and-structured-data/programs/pydantic_schema.py), [structured output](../output-parsers-and-structured-data/programs/structured_output_with_raw.py) | Main patterns; Class 17 has no numbered PDF in the archive. |
| 19–25 | LCEL and runnable composition | [Pipeline](../lcel-and-runnables/programs/lcel_pipeline.py), [execution modes](../lcel-and-runnables/programs/execution_modes.py), [sequence](../lcel-and-runnables/programs/runnable_sequence.py), [parallel](../lcel-and-runnables/programs/runnable_parallel.py), [passthrough](../lcel-and-runnables/programs/runnable_passthrough.py), [branch](../lcel-and-runnables/programs/runnable_branch.py) | Main patterns; some PDF variants require a model key. |
| 29 | Message concepts and review | [Message roles](../getting-started/programs/message_roles.py) | PDF is a quiz. |
| 30–33 | Stateless calls, dynamic history, recent window, system message | [Four offline exercises](class30_33_history.py), [live manual history](../conversation-history-and-memory/programs/manual_chat_history.py), [window](../conversation-history-and-memory/programs/recent_history_window.py) | Adapted exercises; live behavior needs a model key. |
| 34–36 | Legacy memory and ConversationChain | [Legacy memory](../conversation-history-and-memory/programs/legacy_memory_examples.py), [ConversationChain](../conversation-history-and-memory/programs/legacy_conversation_chain.py) | Historical API; needs a compatible separate environment. |
| 37–41 | Session history, serialization, persistence | [Session history](../conversation-history-and-memory/programs/session_history.py), [multi-user](../conversation-history-and-memory/programs/multi_user_chat.py), [serialization](../conversation-history-and-memory/programs/message_serialization.py), [file history](../conversation-history-and-memory/programs/file_chat_history.py) | Main patterns; not every PDF variation is separate. |
| 42–43 | Review and multi-user chatbot | [Session isolation](../multi-user-chatbots/programs/session_isolation.py), [persistent chatbot](../conversation-history-and-memory/programs/persistent_chatbot.py) | Class 42 is a quiz; Class 43 app is adapted. |
| 44–45 | Supabase chatbot and RAG overview | [Source PDFs](../lessons/classes-42-62.md) | Complete Supabase and RAG apps are not standalone programs. |
| 46–47 | Source gap and fundamentals image | [Source map](../lessons/classes-42-62.md) | No Class 46 source; Class 47 has an image only. |
| 48 | `Document` objects | [Five exercises](class48_documents.py) | Five numbered PDF topics. |
| 49 | `TextLoader` | [Five exercises](class49_text_loader.py) | First load, metadata, multiple files, missing file, lazy load. |
| 50–51 | `PyPDFLoader` | [Five exercises](class50_51_pdf_loader.py) | Both PDFs repeat the five key topics. |
| 52 | `CSVLoader` | [Four exercises](class52_csv_loader.py) | Basic, actual CSV, selected columns, source and delimiter. |
| 53 | `WebBaseLoader` | [Four exercises](class53_web_loader.py) | Uses a local demo website; needs loopback network access. |
| 54 | Custom text `BaseLoader` | [Single and folder loader](class54_custom_text_loader.py) | Two custom-loader patterns. |
| 55 | Core PDF parsing | [Four exercises](class55_pdf_core.py) | Single page, many pages, whole PDF, custom loader. |
| 56 | Custom CSV loader | [Custom loader](../rag-and-document-loading/programs/custom_loaders.py) | Image source only. |
| 57 | HTML and web Documents | [Three exercises](class57_web_documents.py) | Local HTML, fetched page, custom web loader; needs loopback network access. |
| 58 | Metadata normalization | [Four exercises](class58_metadata.py) | Enrich, page/row numbering, standardize, inspect. |
| 59 | Splitting review | [Text splitting guide](../text-splitting/notes.md) | Image source only. |
| 60 | Splitting fundamentals | [Five exercises](../text-splitting/programs/class_60_five_programs.py) | All five named PDF topics. |
| 61 | Chunk size/overlap concepts | [Text splitting guide](../text-splitting/notes.md) | PDF has conceptual examples, not numbered full programs. |
| 62 | `CharacterTextSplitter` | [Eight exercises](../text-splitting/programs/class_62_eight_programs.py) | All eight named PDF topics. |

**Coverage limit:** These files make the principal exercises easy to run. They do not reproduce every line or small variation from the classroom PDFs. For exact source code and outputs, open the relevant PDF in [`sources/pdfs`](../sources/pdfs).
