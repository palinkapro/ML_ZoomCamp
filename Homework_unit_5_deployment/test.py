import requests
import json

#flask
#customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}

#docker
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}


url = 'http://localhost:9696/predict'


response = requests.post(url, json=customer)
result = response.json()

print(json.dumps(result, indent=2))