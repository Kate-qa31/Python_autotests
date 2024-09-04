import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '38e21b2f91b311cecd7b640e7051702a'
HEADER = {'Content_type':'application/json', 'trainer_token':TOKEN}

body_creation = {
    "name": "Снежок",
    "photo_id": 256
}

body_changing = {
    "pokemon_id": "67413",
    "name": "Пирожочек",
    "photo_id": 256
}

body_catching = {
    "pokemon_id": "67413"
}


creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print (creation.text)

changing = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changing)
print (changing.text)

catching = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catching)
print (catching.text)

