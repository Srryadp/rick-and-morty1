import requests
import time
import os

# Hacer una solicitud a la API
response = requests.get("https://rickandmortyapi.com/api/episode")
data = response.json()  # Esto convierte la respuesta JSON en un diccionario de Python

def limpiar_pantalla():
    return os.system('cls' if os.name == 'nt' else 'clear')



# Hacer una solicitud a la API para obtener el episodio con ID 19

while True:

    episode_id = input("Ingrese el id que quiera :D : ")

    episode_response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
    episode_data = episode_response.json()

    
    if episode_id == "8":
        
        print()
        print("\nDatos del episodio con ID 8:\n")
        print("ID:", episode_data["id"])
        print()
        print("Nombre:", episode_data["name"])
        print("Fecha de emision:", episode_data["air_date"])
        print("Episodio:", episode_data["episode"])
        print()
        
        for url, character_url in enumerate(episode_data["characters"], start=1):
            
            print(f"{url}. {character_url}")

        
        num_episodes = len(episode_data["episode"])


        print()
        print(f"cantidad de espiodios del sujeto {episode_id}:", num_episodes)
        time.sleep(4)
        limpiar_pantalla()
    

    elif episode_id == "19":

        print(f"\nDatos del episodio con ID {episode_id}\n")
        print("ID:", episode_data["id"])
        print()
        print("Name:", episode_data["name"])
        print("Air date:", episode_data["air_date"])
        print("Episode:", episode_data["episode"])
        print()

        print("URLs de los personajes")
        
        for url, character_url in enumerate(episode_data["characters"], start=1):
            
            print(f"{url}. {character_url}")

        num_episodes = len(episode_data["episode"])


        print()
        print(f"cantidad de espiodios del sujeto {episode_id}:", num_episodes)
        print()
        print("Created", episode_data["created"])
        time.sleep(4)
        limpiar_pantalla()

    else:

        # Imprimir los datos del episodio con formato legible
        print(f"\nDatos del episodio con ID {episode_id}\n")
        print("Identificador:", episode_data["id"])
        print()
        print("Nombre:", episode_data["name"])
        print("Fecha de emision:", episode_data["air_date"])
        print("Episodio:", episode_data["episode"])
        print()

        for url, character_url in enumerate(episode_data["characters"], start=1):
            
            print(f"{url}. {character_url}")

        print()
        num_episodes = len(episode_data["episode"])


        print()
        print(f"cantidad de espiodios del sujeto {episode_id}:", num_episodes)
        input("")
        print("Created", episode_data["created"])
        time.sleep(4)
        limpiar_pantalla()