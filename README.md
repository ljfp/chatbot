## Chatbot function-call demo

Minimal CLI chatbot that uses Google GenAI tools to call local helper functions (list files, read files, write files, run Python). The tool functions are implemented under the calculator sandbox.

### Project layout

- [main.py](main.py): CLI entrypoint and GenAI request loop.
- [call_function.py](call_function.py): Maps model tool calls to local functions and injects the calculator working directory.
- [prompts.py](prompts.py): System prompt used for the model.
- [functions](functions): Tool implementations and schemas.
- [calculator](calculator): Sandbox workspace used by tools.

### Requirements

- Python 3.13+
- A Gemini API key in environment variable `GEMINI_API_KEY`

### Install

Use your preferred Python environment, then install dependencies from [pyproject.toml](pyproject.toml).

### Usage

Run the CLI with a single prompt:

```
python main.py "List files in the sandbox and show calculator/main.py"
```

Enable verbose logging:

```
python main.py "Summarize calculator/pkg/calculator.py" --verbose
```

### Notes

- Tool calls are constrained to the calculator directory by [call_function.py](call_function.py).
- The model prompt is defined in [prompts.py](prompts.py).
