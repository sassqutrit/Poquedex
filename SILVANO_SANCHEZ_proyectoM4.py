import requests
import json
import os

def obtener_datos_pokemon(nombre):
    # Hacer la petición a la API
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    # Verificar el status code
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Extraer la información relevante o mostrar los datos de un pokemon
def mostrar_datos_pokemon(datos):
    print(f"Nombre: {datos['name'].capitalize()}")
    print(f"Peso: {datos['weight']} hectogramos")
    print(f"Altura: {datos['height']} decímetros")
    print("Tipos: ", ", ".join([tipo['type']['name'] for tipo in datos['types']]))
    print("Habilidades: ", ", ".join([habilidad['ability']['name'] for habilidad in datos['abilities']]))
    print("Movimientos: ", ", ".join([movimiento['move']['name'] for movimiento in datos['moves'][:5]]))  # Mostrando solo 5 movimientos
    print(f"Imagen: {datos['sprites']['front_default']}")

# Guarda los datos de pokemon en un archivo .json que se encuentra dentro de una carpeta
def guardar_datos_pokemon(datos):
    # Crea la carpeta si esta no existe
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    # Guarda la información en un archivo .json
    nombre_archivo = f"pokedex/{datos['name']}.json"
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Función principal para introducir el nombre del pokemon y obtener sus datos
def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    datos_pokemon = obtener_datos_pokemon(nombre_pokemon)

    if datos_pokemon:
        mostrar_datos_pokemon(datos_pokemon)
        guardar_datos_pokemon(datos_pokemon)
        print(f"Datos de {nombre_pokemon.capitalize()} guardados en pokedex/{nombre_pokemon}.json")
    else:
        print("Pokémon no encontrado. Por favor, verifica el nombre e inténtalo de nuevo.")

# Se ejecuta la función principal si esta contiene ese mismo nombre
if __name__ == "__main__":
    main()
