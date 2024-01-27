import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-my_github.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, password))
if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])
else:
    print(None)
