# Running Tests

## Setup
1. Install dependencies:
   ```bash
   uv sync
   ```

2. Copy the environment template and add your API keys:
   ```bash
   cp env.template .env
   ```
   Add your Anthropic and OpenAI API keys to the `.env` file.

## Running Tests
To run the test suite:
```bash
uv run pytest
```



