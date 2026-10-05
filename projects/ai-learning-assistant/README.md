# AI learning assistant

Adapted from the supplied [60-minute workshop](../../sources/pdfs/GENAI-Langchain-workshop.pdf). The user enters a topic and learner level. The application asks a model for a plain-language explanation, five key points, and a practical example.

Run from the repository root after setting `OPENAI_API_KEY`:

```powershell
python projects/ai-learning-assistant/assistant.py
```

The example keeps the prompt and model call visible, so it is easy to compare with the earlier topic programs. Model output is explanatory text, not a validated structured record.
