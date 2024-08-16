#this python file if for testing whatever small or large code snippet is not working as expected
import requests

url = "https://api-inference.huggingface.co/models/gpt2"
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}
payload = {
    "inputs": "Hello, how are you?"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
