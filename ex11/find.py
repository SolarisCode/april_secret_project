import requests

url = "https://pokeapi.co/api/v2/pokemon/"
peko = input("Enter the name of a Pokemon: ")
url = "".join([url, peko.lower()])

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    abilities = data["abilities"]
    for item in abilities:
        print(item["ability"]["name"].capitalize())
else:
    print(f"API return invaild code {response.status_code}."\
    "\nPlease double check the pokemon name.")
