# Text splitting: classes 59–66

## Why split text?

The [Class 59 revision infographic](../sources/images/class%2059.png) connects document loading to chunking. A large Document is difficult to search as one unit and may waste model context. Splitting produces smaller pieces that can be indexed and retrieved individually. The [Class 60 lesson](../sources/pdfs/Langchain%20-%20class60.pdf) introduces four terms: a **chunk** is one piece; **chunk size** is the target length; **chunk overlap** repeats some content between neighboring chunks; and a **separator** marks a preferred split point.

Chunk size is measured by the configured `length_function`. With Python `len`, it counts characters, not model tokens. Chunks can vary in length, and a splitter that only cuts at one separator can return a piece larger than the target. These are key [Class 61 mistakes and limitations](../sources/pdfs/Langchain%20-%20class61.pdf). Choose size and overlap for the material and retrieval task, then test retrieval quality rather than assuming one setting is best.

## CharacterTextSplitter

[Class 62](../sources/pdfs/Langchain%20-%20class62.pdf) explains `CharacterTextSplitter`: it splits at a configured separator and merges pieces toward the target chunk size. `split_text()` returns strings. `create_documents()` creates Documents from text and optional metadata. `split_documents()` accepts Documents and preserves their source metadata. The [short demo](programs/splitting_demo.py) shows metadata and an oversized-piece case. The [Class 60 five-program practice](programs/class_60_five_programs.py) and [Class 62 eight-program practice](programs/class_62_eight_programs.py) cover the programs named in the ChatGPT notes.

For text with mixed paragraph, line and word boundaries, `RecursiveCharacterTextSplitter` tries a sequence of separators. It is a useful follow-up when one separator leaves pieces too large. The original Class 62 PDF contains the complete classroom programs and outputs. The repository scripts are checked adaptations, with an [explicit source and program map](../lessons/program-source-map.md).

## Recursive splitting and chunk experiments: classes 64-66

[Class 64](../sources/pdfs/Langchain%20-%20class64.pdf) extends the single-separator lesson. `RecursiveCharacterTextSplitter` tries separators in order, typically paragraphs, lines, spaces, then individual characters. When a piece remains too large, it falls back to the next separator. The [Class 64 infographic](../sources/images/class%2064.png) shows this flow; [Class 65](../sources/pdfs/Langchain%20-%20class65.pdf) introduces ChunkViz as a visual aid. An online visualization is useful for learning, but inspect the output of your actual splitter because its settings and version determine your chunks.

[Class 66](../sources/pdfs/Langchain%20-%20class66.pdf) compares chunk size and overlap. Small chunks can separate related facts; large chunks can mix unrelated topics. More overlap repeats context but increases index size and potentially retrieval cost. There is no universally best setting: inspect boundary quality and test the questions your application must answer. The [recursive splitting demo](programs/recursive_splitting.py) runs offline and retains `Document` metadata.

The [Class 64 eight-program practice](programs/class_64_eight_programs.py) follows the PDF's sequence: first recursive split, comparison with `CharacterTextSplitter`, separator priority, deeper fallback, overlap, `keep_separator`, metadata, and a policy document. The [Class 66 experiments](programs/class_66_experiments.py) vary chunk size and overlap on fixed text and sample policy/FAQ material. Both run offline.

## Practice checks

1. Given `chunk_size=100` and `length_function=len`, what is measured?
2. Why might a 120-character paragraph remain one chunk with a paragraph-only separator?
3. Which method should you use to preserve the metadata of an existing Document?
4. What happens to retrieval context when overlap is too small or excessively large?
