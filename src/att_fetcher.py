import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        attributes = {
            "Name": data["name"].capitalize(),
            "ID": data["id"],
            "Height": data["height"],
            "Weight": data["weight"],
            "Base Experience": data["base_experience"],
            "Types": [t["type"]["name"].capitalize() for t in data["types"]]
        }
        return attributes
    else:
        return f"Error: Pokémon '{pokemon_name}' not found."

if __name__ == "__main__":
    pokemon_name = input("Enter Pokémon name: ")
    info = get_pokemon_info(pokemon_name)
    print(info)
