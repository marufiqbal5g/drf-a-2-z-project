import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    "title": "Hello World from drf",
    "price": 123
}

get_response = requests.put(endpoint, json=data)

print(f'text only:{get_response.text}')
print(f'status code: {get_response.status_code}')
print(f'json: {get_response.json()}')