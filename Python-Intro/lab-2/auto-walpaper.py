import requests

api_url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": "53dTw4dcmpEFvWp4qeLu9cypAG3wXbkbk3qRMDhc"
}

response = requests.get(api_url, params=params)

print("Status Code:", response.status_code)

data = response.json()  
print(data)
