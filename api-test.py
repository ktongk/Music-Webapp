import requests
import json

# API_KEY = '481f402ee33742c5befd623eb166f241'
url =  \
    "https://api.genius.com/search?q=Kendrick%20Lamar"

my_headers = {
    "Authorization": "Bearer JiwPumUVzR09r0Amrig4U14cGcYdoiNVcGTtncZUwYMNTt0SuEVmeuOV7kAPI4HW"
}

response = requests.get(url, headers=my_headers)
json_body = response.json()
#print(json.dumps(json_body, indent=2))
print(json_body["name"][0]["title"])