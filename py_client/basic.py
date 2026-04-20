import requests

endpoint = 'http://localhost:8000/api/'

get_response = requests.get(endpoint, json={"query": "hello world"})
print(f'text only:{get_response.text}')
print(f'status code: {get_response.status_code}')
print(f'json: {get_response.json()}')