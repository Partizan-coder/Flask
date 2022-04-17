import requests

HOST = 'http://127.0.0.1:8080'

resp = requests.post(f'{HOST}/test')

print(resp.status_code)