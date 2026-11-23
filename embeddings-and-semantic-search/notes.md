# Embeddings and semantic search: classes 67–74

An embedding model turns text into a numeric vector. Similarity functions compare vectors, allowing a search system to rank document chunks by meaning. The [Class 67](../sources/images/class%2067.png) and [Class 68](../sources/images/RAG%20Embeddings%20and%20Cosine%20Similarity%20Infographic%2068%20demo.png) infographics connect loading, splitting, embeddings, retrieval, and a grounded answer. Embeddings produce vectors; a chat model produces the answer.

## Understand the comparison first

[Class 69](../sources/pdfs/Langchain%20-%20class69.pdf) introduces vector components and cosine similarity. Cosine similarity is the dot product divided by the vectors' magnitudes. It requires equal dimensions and nonzero vectors. A higher score often indicates closer meaning for vectors from the same embedding model, but it is not a calibrated truth probability. [Class 70](../sources/pdfs/Langchain%20-%20class70.pdf) contrasts keyword matching, Jaccard word overlap, and meaning-based retrieval. Exact IDs and codes may benefit from keyword search even when semantic search helps with paraphrases. Run the [offline similarity demo](programs/similarity_basics.py) before calling an embedding API.

The [Class 69 five-program practice](programs/class_69_five_programs.py) covers manual vectors, dimensions, document chunks, and cosine math. The [Class 70 seven-program practice](programs/class_70_seven_programs.py) covers keyword misses, word overlap, ambiguity, a manually defined synonym lookup, and a search-flow preview. Neither script produces semantic embeddings. The optional plotting and NumPy extras from Class 69 remain in the original PDF; they are not part of the base dependencies.

## Generate embeddings

The [Class 71 infographic](../sources/images/class%2071.png) and [Class 72 notes](../sources/pdfs/Langchain%20-%20class72.pdf) compare hosted and local models. `OpenAIEmbeddings.embed_query(text)` embeds one question; `embed_documents(texts)` embeds a list of strings. A hosted model needs an API key, network access, and may incur cost. Keep keys out of Git. The [query example](programs/query_embedding.py) prints vector dimensions and a short sample without dumping the whole vector.

[Class 73](../sources/images/class%2073.png) and [Class 74](../sources/pdfs/Langchain%20-%20class74.pdf) combine `Document` objects, splitting, and document embeddings. Pass `page_content` strings to `embed_documents()`, then pair the resulting vectors with each chunk and its metadata. Use the same embedding model and compatible dimensions for stored chunks and later queries. The [document pipeline](programs/document_embeddings.py) demonstrates this without a vector database. The diagrams show [Class 69](../sources/images/class%2069.png), [70](../sources/images/class%2070.png), and [72](../sources/images/class%2072.png) concepts at a glance.

The [Class 72 seven practicals](programs/class_72_seven_practicals.py) include six hosted-model exercises and an optional local Hugging Face model exercise (`--local`). The local option needs `langchain-huggingface` and `sentence-transformers`, which are not in the base requirements. The [Class 74 seven-program practice](programs/class_74_seven_programs.py) follows the PDF's document embedding sequence and keeps all records in memory.

## Try it

From the repository root, install `requirements.txt`, set `OPENAI_API_KEY` in your environment for hosted examples, then run:

```powershell
python embeddings-and-semantic-search/programs/similarity_basics.py
python embeddings-and-semantic-search/programs/query_embedding.py
python embeddings-and-semantic-search/programs/document_embeddings.py
python text-splitting/programs/class_64_eight_programs.py
python text-splitting/programs/class_66_experiments.py
python embeddings-and-semantic-search/programs/class_69_five_programs.py
python embeddings-and-semantic-search/programs/class_70_seven_programs.py
python embeddings-and-semantic-search/programs/class_72_seven_practicals.py
python embeddings-and-semantic-search/programs/class_74_seven_programs.py
```

The similarity, Classes 64, 66, 69, and 70 programs are offline. The query, document, Class 72, and Class 74 programs call an embedding API unless `--local` is used for Class 72. The original PDFs remain the complete classroom reference; repository scripts are focused adaptations.
