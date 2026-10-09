# LCEL and runnables

![Class 19 overview](../sources/images/class%2019.png)

## Compose a pipeline

LCEL uses the `|` operator to connect compatible components. `prompt | model | parser` creates a chain; the chain runs when invoked. The output of each component becomes the next component's input. Run [lcel_pipeline.py](programs/lcel_pipeline.py) for a live model example.

## Common execution methods

| Method | Input | Output | Typical use |
| --- | --- | --- | --- |
| `invoke` | One input | One final result | A normal request |
| `batch` | List of inputs | List of results | Multiple independent requests |
| `stream` | One input | Chunks as available | Interactive display |

Run [execution_modes.py](programs/execution_modes.py) without an API key. Batch processing may still make a separate model call per item; speed depends on limits and provider behavior.

## Sequence or parallel?

![Class 23 overview](../sources/images/class%2023.png)

Use a sequence when each step needs the previous result. `RunnableLambda` adapts a Python function to a runnable, and `RunnableSequence` chains compatible steps. Run [runnable_sequence.py](programs/runnable_sequence.py).

![Class 25 overview](../sources/images/class%2025.png)

Use `RunnableParallel` when branches can work from the same input independently. It returns a dictionary keyed by branch name. Run [runnable_parallel.py](programs/runnable_parallel.py). A mixed workflow can produce one explanation, then branch into a summary and questions.

## Preserve input, then branch (September 22 lesson)

`RunnablePassthrough` forwards its input unchanged. Put it beside a transforming runnable in `RunnableParallel` when later steps need both the original and changed values. Run [runnable_passthrough.py](programs/runnable_passthrough.py) without an API key. The [AI content multiplier](programs/ai_content_multiplier.py) first generates an explanation, then runs summary, quiz, social-post, and interview-question branches on that explanation. Its branches each make a model call; parallel work can reduce waiting time but does not remove model cost.

`batch()` applies **one runnable to many inputs**. `RunnableParallel` applies **multiple runnables to the same input**. A sequence is still needed before a parallel stage when the branches depend on a shared intermediate result.

## Choose one path (September 24 lesson)

`RunnableBranch` checks conditions in order and executes the first matching runnable. The final runnable is the default path. Put narrow conditions before broad ones: `>= 75` must precede `>= 35` in a grading rule. Run the offline [grading and dictionary-input example](programs/runnable_branch.py), then the live [study material router](programs/study_material_router.py). Validate user choices before routing so an unsupported level does not silently receive advanced material.

These two lessons came from the [ChatGPT LangChain project](../lessons/README.md), where the notes include RunnablePassthrough, the AI Content Multiplier, and six RunnableBranch demonstrations. The local source archive has no separate PDF for these dates.

## Source material

- [Class 19](../sources/pdfs/Langchain%20-%20class19.pdf), [class 20](../sources/pdfs/LC%20Sept16%20notes.pdf), [classes 21–25](../sources/README.md#lcel-and-runnables)
