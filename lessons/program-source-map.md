# Program and source map for newer lessons

The original local folder, `AI DUrga sir`, supplies the classroom PDFs and infographics archived in [`sources/`](../sources/README.md). Its top level has no standalone Python files for these lessons; many programs are printed inside the PDFs. The **Langchain Durga sir** ChatGPT collection also contains formatted study notes. Repository `.py` files are runnable adaptations or focused demonstrations, not a verbatim export of every classroom script.

The [class-by-class Python practice guide](../practice/README.md) now includes the loader and metadata exercises from Classes 48–58. The [searchable PDF text](../practice/pdf-text/README.md) preserves the extractable text of every page of each numbered PDF, including source program listings; check the PDFs where extraction changes code formatting.

The [ChatGPT-to-GitHub review](chatgpt-classes-45-62.md) maps Classes 45–62 to the chats in the **Langchain Durga sir** project and Library folder, then to the matching Python practice files.

| Class or topic | Original PDF and image | Runnable programs in this repository |
| --- | --- | --- |
| 42: history review | [PDF](../sources/pdfs/Langchain%20-%20class42.pdf) | [Manual history](../conversation-history-and-memory/programs/manual_chat_history.py), [window](../conversation-history-and-memory/programs/recent_history_window.py), [serialization](../conversation-history-and-memory/programs/message_serialization.py), [file store](../conversation-history-and-memory/programs/file_chat_history.py) |
| 43: multi-user file history | [PDF](../sources/pdfs/Langchain%20-%20class43.pdf), [image](../sources/images/class%2043.png) | [File history](../conversation-history-and-memory/programs/file_chat_history.py), [persistent chatbot](../conversation-history-and-memory/programs/persistent_chatbot.py), [session isolation](../multi-user-chatbots/programs/session_isolation.py) |
| 44: Supabase chatbot | [PDF](../sources/pdfs/Langchain%20-%20class44.pdf), [image](../sources/images/Class%2044%20-Python%20Supabase%20Chatbot%20Flow%20Infographic.png) | [Message serialization](../conversation-history-and-memory/programs/message_serialization.py) only; the complete Supabase application remains in the PDF and is **not** a standalone repository program. |
| 45: RAG orientation | [PDF](../sources/pdfs/Langchain%20-%20class45%20-%20RAG.pdf), [image](../sources/images/class%2045-RAG.png) | Concept guide; no complete RAG application added. |
| 48–56: Documents, TXT, PDF and CSV | [Class-by-class source list](classes-42-62.md) | [Custom TXT/CSV loaders](../rag-and-document-loading/programs/custom_loaders.py), [PDF documents](../rag-and-document-loading/programs/pdf_documents.py) |
| 57–58: HTML and metadata | [Class-by-class source list](classes-42-62.md) | [HTML document](../rag-and-document-loading/programs/html_document.py), [document inspector](../rag-and-document-loading/programs/inspect_documents.py) |
| 60: splitting fundamentals | [PDF](../sources/pdfs/Langchain%20-%20class60.pdf), [image](../sources/images/class%2060.png) | [Five-program practice](../text-splitting/programs/class_60_five_programs.py) |
| 62: `CharacterTextSplitter` | [PDF](../sources/pdfs/Langchain%20-%20class62.pdf), [image](../sources/images/class%2062.png) | [Eight-program practice](../text-splitting/programs/class_62_eight_programs.py), [short demo](../text-splitting/programs/splitting_demo.py) |

## ChatGPT collection program references

The [Class 60 ChatGPT note](https://chatgpt.com/g/g-p-6a99b83f104c81919a85411523ecc95d/c/6ae8c721-9dc8-83ea-9ff3-9a90e03f4672) names five programs: fixed-size Python chunking; overlap; separator behavior; first LangChain splitter; and splitting Document objects. The [five-program practice script](../text-splitting/programs/class_60_five_programs.py) covers those five ideas.

The [Class 62 ChatGPT note](https://chatgpt.com/g/g-p-6a99b83f104c81919a85411523ecc95d/c/6aeb86b4-b1a0-83ea-bb63-801b4a44f6ee) names eight programs: first `CharacterTextSplitter`; default separator; missing separator; space separator; overlap; `keep_separator`; `split_documents()` with metadata; and `add_start_index`. The [eight-program practice script](../text-splitting/programs/class_62_eight_programs.py) covers all eight topics. The complete classroom explanations and outputs remain in the [Class 62 PDF](../sources/pdfs/Langchain%20-%20class62.pdf).

For Classes 47, 56 and 59, the local folder supplied an infographic but no numbered PDF. Class 46 had neither. See the [lesson map](classes-42-62.md) for those source gaps.
