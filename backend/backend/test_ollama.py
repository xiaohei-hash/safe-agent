import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "deepseek-r1",
        "prompt": "hello",
        "stream": False
    }
)

print(response.json())