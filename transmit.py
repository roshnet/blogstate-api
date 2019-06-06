import requests

payload = {
    'u': 'userone',
    'p': 'userone'
}

resp = requests.post('http://localhost:5000/api/login', json=payload)

print(resp.status_code)
print(resp.headers['auth-status'])
