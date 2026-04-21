import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "New Product",
    "price": 123,

}

get_response = requests.post(endpoint, json=data)

print(f'text only:{get_response.text}')
print(f'status code: {get_response.status_code}')
print(f'json: {get_response.json()}')