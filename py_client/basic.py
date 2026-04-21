import requests

endpoint = 'http://localhost:8000/api/'

get_response = requests.post(endpoint, json={"title": "New Product", "content": "hello world", "price": 123})
print(f'text only:{get_response.text}')
print(f'status code: {get_response.status_code}')
print(f'json: {get_response.json()}')