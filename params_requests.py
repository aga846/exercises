import requests

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}      # to to samo co wpisanie w 3 linijce
                                            # po search "?term=cat&limit=1"
)

data = response.json()
print(data["results"][0]["joke"])

'''
requests.get(
    http://www.example.com",
    params={
        "key1": "value1",
        "key2": "value2"
    }
)
'''
