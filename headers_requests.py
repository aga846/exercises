import requests

url = "https://icanhazdadjoke.com"
response = requests.get(url, headers={"Accept": "text/plain"})

print(response.text)


# response = requests.get(url, headers={"Accept": "application/json"})
# print(response.text) - tu dostaje jeden wielki string, mimo ze wyglada jak slownik
# print(response.json()) - tu dostaje to co wyzej, ale jako pythonowy slownik
# data = response.json() - data to pythonowy slownik

# requests.get(
    # http://www.example.com",
    # params={
        # "key1": "value1",
        # "key2": "value2"
    # }
# )
