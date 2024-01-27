import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

response = requests.post(url, data=data)

try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response['id'], json_response['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
