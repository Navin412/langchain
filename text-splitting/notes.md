# Text splitting: classes 59–62

## Why split text?

The [Class 59 revision infographic](../sources/images/class%2059.png) connects document loading to chunking. A large Document is difficult to search as one unit and may waste model context. Splitting produces smaller pieces that can be indexed and retrieved individually. The [Class 60 lesson](../sources/pdfs/Langchain%20-%20class60.pdf) introduces four terms: a **chunk** is one piece; **chunk size** is the target length; **chunk overlap** repeats some content between neighboring chunks; and a **separator** marks a preferred split point.

Chunk size is measured by the configured `length_function`. With Python `len`, it counts characters, not model tokens. Chunks can vary in length, and a splitter that only cuts at one separator can return a piece larger than the target. These are key [Class 61 mistakes and limitations](../sources/pdfs/Langchain%20-%20class61.pdf). Choose size and overlap for the material and retrieval task, then test retrieval quality rather than assuming one setting is best.

## CharacterTextSplitter

[Class 62](../sources/pdfs/Langchain%20-%20class62.pdf) explains `CharacterTextSplitter`: it splits at a configured separator and merges pieces toward the target chunk size. `split_text()` returns strings. `create_documents()` creates Documents from text and optional metadata. `split_documents()` accepts Documents and preserves their source metadata. The [offline examples](programs/splitting_demo.py) show these methods and an oversized-piece case.

For text with mixed paragraph, line and word boundaries, `RecursiveCharacterTextSplitter` tries a sequence of separators. It is a useful follow-up when one separator leaves pieces too large. The original Class 62 PDF contains eight classroom programs and outputs; the included program provides a smaller checked practice set.

## Practice checks

1. Given `chunk_size=100` and `length_function=len`, what is measured?
2. Why might a 120-character paragraph remain one chunk with a paragraph-only separator?
3. Which method should you use to preserve the metadata of an existing Document?
4. What happens to retrieval context when overlap is too small or excessively large?
