import requests
import datetime

HOST = 'http://127.0.0.1:8080'

# resp = requests.post(f'{HOST}/test')

resp = requests.delete(f'{HOST}/announcement/1/delete')

# resp = requests.get(f'{HOST}/announcement/1')

# resp = requests.post(f'{HOST}/announcement', json={
#     'Header': 'header_1',
#     'Description': 'description_1',
#     # 'Create_date': f'{datetime.datetime.now()}',
#     'Owner': 'owner_1'
# })

print(resp.status_code)
print(resp.text)