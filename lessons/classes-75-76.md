# LangChain classes 75–76

| Class | Topic | Source |
| --- | --- | --- |
| 75 | Manual retrieval, cosine similarity, and Euclidean distance | [Infographic](../sources/images/class%2075.png) |
| 76 | Similarity scores, document ranking, and the move toward vector stores | [PDF](../sources/pdfs/Langchain%20-%20class76.pdf), [infographic](../sources/images/class%2076.png) |

The [Class 76 Python script](../embeddings-and-semantic-search/programs/class_76_similarity_search.py) adapts all seven numbered programs from the PDF.

| Programs | Practice | PDF pages |
| --- | --- | --- |
| 1–3 | Calculate cosine similarity, reuse the cosine function, and compare cosine, dot product, and Euclidean distance | 2–4 |
| 4 | Compare embeddings of related and unrelated sentences | 4–5 |
| 5–6 | Rank documents by cosine similarity and select the top K | 5–7 |
| 7 | Split course documents, embed the chunks, and retrieve matches with source and category metadata | 7–11 |

Install the repository's [requirements](../requirements.txt) and run from the repository root.

```powershell
python embeddings-and-semantic-search/programs/class_76_similarity_search.py
```

For exercises 4–7, set `OPENAI_API_KEY` in your environment. These exercises make live embedding API calls.

```powershell
python embeddings-and-semantic-search/programs/class_76_similarity_search.py --live --question "Can I attend classes from home?" --top-k 3
```

Cosine similarity ranks larger values first, while Euclidean distance ranks smaller values first. The script performs exact, in-memory ranking and returns retrieved text and metadata.
