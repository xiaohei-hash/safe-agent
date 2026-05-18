import requests
import json

SYSTEM_PROMPT = """
You are a tool-calling AI agent.

CRITICAL RULES:

1. Output ONLY valid JSON
2. No explanation
3. No markdown
4. No code block
5. No natural language
6. No <think>
7. No analysis

You must answer ONLY in this exact format:

{
  "tool": "write_file",
  "args": {
    "path": "workspace/example.txt",
    "content": "hello world"
  }
}

NEVER output anything else.
"""


class LLMClient:

    def generate(self, prompt: str):

        full_prompt = SYSTEM_PROMPT + "\n\nUSER REQUEST:\n" + prompt

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "deepseek-r1:latest",
                "prompt": full_prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()

        print(json.dumps(data, indent=2, ensure_ascii=False))

        return data["response"]