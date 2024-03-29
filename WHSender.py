import requests

url = "webhook url"

data = {
  "the data"
}

x = requests.post(url, json=data)

print(x)
