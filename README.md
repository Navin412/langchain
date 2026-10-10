# LangChain learning notes and programs

Topic-based study material adapted from the supplied *AI with Durga Sir* class notes. Start with the topics below and run the small programs as you go. The original PDFs and images are preserved in [`sources/`](sources/README.md) for reference.

| Order | Topic | Classes | What you will practice |
| --- | --- | --- | --- |
| 1 | [Getting started](getting-started/notes.md) | 3–7 | Models, messages, context, and first calls |
| 2 | [Prompts and messages](prompts-and-messages/notes.md) | 8–12 | Reusable text and chat prompts |
| 3 | [Output parsers and structured data](output-parsers-and-structured-data/notes.md) | 13–18 | AIMessage, parsing, Pydantic, structured output |
| 4 | [LCEL and runnables](lcel-and-runnables/notes.md) | 19–25, September 22–24 | Chains, execution modes, sequence, parallel, passthrough, conditional routing |
| 5 | [Conversation history and memory](conversation-history-and-memory/notes.md) | 29–41 | Manual history, windows, sessions, JSON serialization, persistence |
| 6 | [AI learning assistant](projects/ai-learning-assistant/README.md) | Workshop | A complete small application |

See the [lesson map](lessons/README.md) for additional material from the ChatGPT project. Classes 39–41 now have archived source PDFs; classes 39 and 40 also have infographics. It links each lesson to the matching topic guide and programs.

## Run the examples

Requires Python 3.10 or newer. From this folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Examples that call a model require an OpenAI API key in the `OPENAI_API_KEY` environment variable. Never commit an API key or a `.env` file.

```powershell
$env:OPENAI_API_KEY = "your-key"
python prompts-and-messages/programs/restaurant_names.py
```

Programs that only format prompts or demonstrate runnables can run without an API key. The dependency versions in `requirements.txt` are the versions used to check these examples. The source notes span both current and legacy LangChain APIs; legacy memory examples are explained in the memory guide rather than presented as the default approach.

The file-backed chatbot writes conversations under `chat_history/`, which Git ignores. The optional historical `legacy_memory_examples.py` needs a separate environment with `langchain-classic`; it is not part of the pinned base dependencies.

## How this repository is organized

Each topic has a `notes.md` guide and a `programs/` directory. Guides summarize ideas, show the flow of data, link to source PDFs and images, and point to programs. The source archive keeps the supplied filenames and contents intact. Some WhatsApp images duplicate class images; both originals are retained in `sources/images/` and identified in the [source index](sources/README.md).

The notes are educational examples. Validate model output, costs, and API behavior for your own application before using it in production.
