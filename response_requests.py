import requests

url = "https://google.com"
response = requests.get(url)

print(f"Your request to {url} came back with status code {response.status_code}")
