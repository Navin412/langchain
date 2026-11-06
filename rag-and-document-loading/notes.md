# RAG and document loading: classes 45–58

## The RAG pipeline

Class 45 introduces retrieval-augmented generation (RAG): load external material, divide it into useful pieces, create embeddings, index those pieces, retrieve relevant material for a question, and pass the retrieved context to a model. The [source lesson](../sources/pdfs/Langchain%20-%20class45%20-%20RAG.pdf) explains why a model cannot answer questions about a private PDF it has not been given. The [Class 47 infographic](../sources/images/class%2047.png) reviews LangChain as an orchestration and abstraction layer, then places RAG beside direct model calls and tool-using agents.

## Documents and loaders

Class 48's core object is `Document(page_content=..., metadata=...)`. `page_content` holds the extracted text; `metadata` identifies its origin and other useful facts. A loader turns a source into one or more Documents. The exact count depends on source and configuration:

| Classes | Source | Classroom result | Source notes |
| --- | --- | --- | --- |
| 49, 54 | Text file | Usually one Document per file | [TextLoader](../sources/pdfs/Langchain%20-%20class49.pdf), [custom BaseLoader](../sources/pdfs/Langchain%20-%20class54.pdf) |
| 50–51, 55 | PDF | Often one Document per page; a single combined document is also possible | [PyPDFLoader intro](../sources/pdfs/Langchain%20-%20class50.pdf), [modes](../sources/pdfs/Langchain%20-%20class51.pdf), [pypdf and core](../sources/pdfs/Langchain%20-%20class55.pdf) |
| 52, 56 | CSV | Usually one Document per data row | [CSVLoader](../sources/pdfs/Langchain%20-%20class52.pdf), [custom CSV infographic](../sources/images/class%2056.png) |
| 53, 57 | Web page | One or more Documents according to the loader and URLs | [WebBaseLoader](../sources/pdfs/Langchain%20-%20class53.pdf), [requests and BeautifulSoup](../sources/pdfs/Langchain%20-%20class57.pdf) |

The later lessons show a path that uses `langchain_core.documents.Document` and Python libraries directly instead of relying on a prebuilt integration. A custom loader can inherit `BaseLoader` and implement `lazy_load()`; the inherited `load()` collects the yielded Documents into a list. See [custom text and CSV examples](programs/custom_loaders.py). The [PDF example](programs/pdf_documents.py) uses `pypdf`, and the [HTML example](programs/html_document.py) parses supplied HTML without a network call.

## Metadata and inspection

Class 58 standardizes source information across TXT, PDF, CSV and HTML, then inspects whether each Document has usable content and metadata. Retain loader-provided fields such as `source`, `page` or `row`; add common fields with `document.metadata.update(...)` instead of replacing the dictionary. The [offline inspector](programs/inspect_documents.py) demonstrates a small consistent schema and a readiness report. Its source is the [Class 58 PDF](../sources/pdfs/Langchain%20-%20class58.pdf), complemented by the [Class 59 revision infographic](../sources/images/class%2059.png).

## Before using retrieved content

Loading a document establishes a text representation, not that extraction was complete or correct. Scanned PDFs may need OCR. Web pages can return navigation text, empty pages or request errors. Review `page_content`, source metadata and permissions before indexing or sending content to a model. Chunking follows in the [text splitting guide](../text-splitting/notes.md).
