# INF601 - Advanced Programming in Python
# Janelyn Nichols
# Final Project

import requests
import json


start = "2024-5-1"
end = "2024-5-1"
accountId = "0"

url = f"https://servitech.com/api/feeds/{start}/{end}/{accountId}"  # API URL

# Servitech bearer token
authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDYzMCIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNTcyNDYwNjk3fQ.Yc0HNp3VyvGMmiss6FalKUL_PVksw9_7D_q_dp7v-Mw"
headers = {  # headers
    'Host': 'servitech.com',
    'Authorization': 'Bearer ' + authToken,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

data = response.json()

with open("servitech_data.json", "w") as file:
    json.dump(data, file)