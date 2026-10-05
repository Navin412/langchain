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

## Source material

- [Class 19](../sources/pdfs/Langchain%20-%20class19.pdf), [class 20](../sources/pdfs/LC%20Sept16%20notes.pdf), [classes 21–25](../sources/README.md#lcel-and-runnables)
