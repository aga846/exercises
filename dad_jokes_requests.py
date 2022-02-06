import requests
from random import choice

user_input = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={
        'Accept': 'application/json',
        'User-Agent': 'MyTest'
    },
    params={"term": user_input}
).json()

print(response)
num_jokes = response["total_jokes"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
    print((choice(response["results"]))["joke"])
elif num_jokes == 1:
    print(f"There is one joke about {user_input}:")
    print(response["results"][0]["joke"])
else:
    print(f"Sorry, coulndn't find a joke with your term: {user_input}")
