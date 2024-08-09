import requests
import time
import os

def limpiar_pantalla():
    
    return os.system('cls' if os.name == 'nt' else 'clear')

def obtener_episodio(episode_id):
   
    episode_response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
   
    if episode_response.status_code == 200:
        episode_data = episode_response.json()
        return episode_data

    else:
        print("\nID no valido...")
        print("\nReseteando programa...")
        time.sleep(4)
        return None

def obtener_personaje(character_id):
   
    character_response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    
    if character_response.status_code == 200:  
        character_data = character_response.json()
        return character_data
    
    else:
        print("\nError al obtener el personaje")
        print("\nReseteando programa...")
        time.sleep(4)
        return None

def beginning():
   
    while True:
       
        limpiar_pantalla()
       
        episode_id = input("Ingrese el ID del episodio que quiera ver: ")
       
        episode_data = obtener_episodio(episode_id)
       
        if episode_data:
            
            print(f"\nDatos del episodio con ID {episode_id}\n")
            print("Identificador:", episode_data["id"])
            print("Nombre:", episode_data["name"])
            print("Fecha de emisión:", episode_data["air_date"])
            print("Episodio:", episode_data["episode"])
            print()
            
            for url, character_url in enumerate(episode_data["characters"], start=1):
               
                print(f"{url}. {character_url}")
               
                character_id = character_url.split("/")[-1]
               
                character_data = obtener_personaje(character_id)
                
                if character_data:
                    
                    print(f"\n  Nombre: {character_data['name']}")
                    print(f"  Especie: {character_data['species']}")
                    print(f"  Género: {character_data['gender']}")
                    print(f"  Estado: {character_data['status']}")
                    print(f"  Origen: {character_data['origin']['name']}")
                    print()
            
            print("\nCantidad de personajes en el episodio:", len(episode_data["characters"]))
            print("Fecha de creación:", episode_data["created"])
            input("\nPresione Enter para continuar...")
            

            time.sleep(4)


if __name__ == "__main__":
    beginning()
