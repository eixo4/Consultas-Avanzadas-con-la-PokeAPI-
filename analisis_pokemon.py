import requests
import time

# Constantes
BASE_URL = "https://pokeapi.co/api/v2/"
HEADERS = {"User-Agent": "PokeAnalisisScript/1.0"}


def obtener_datos(endpoint):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con {url}: {e}")
        return None


def obtener_id_desde_url(url):
    return int(url.rstrip('/').split('/')[-1])

def contar_fuego_kanto():
    print("\n--- 1a. Pokémon tipo Fuego en Kanto ---")
    # Estrategia: Obtener lista de tipo fuego y filtrar los que tienen ID <= 151
    data_fuego = obtener_datos("type/fire")
    if not data_fuego: return

    contador = 0
    kanto_ids = range(1, 152)  # Kanto es del 1 al 151

    for entry in data_fuego['pokemon']:
        p_id = obtener_id_desde_url(entry['pokemon']['url'])
        if p_id in kanto_ids:
            contador += 1

    print(f"Total de Pokémon tipo Fuego en Kanto: {contador}")


def nombres_agua_altura_mayor_10():
    print("\n--- 1b. Pokémon tipo Agua con altura > 10 ---")
    data_agua = obtener_datos("type/water")
    if not data_agua: return

    nombres = []
    # Limitamos a los primeros 20 para no saturar la red en la demo
    pokemons_a_revisar = data_agua['pokemon'][:20]

    print(f"Revisando una muestra de {len(pokemons_a_revisar)} Pokémon de tipo agua...")

    for entry in pokemons_a_revisar:
        nombre = entry['pokemon']['name']
        url = entry['pokemon']['url']

        # Necesitamos hacer una petición extra por cada pokémon para ver su altura
        detalles = requests.get(url).json()
        if detalles['height'] > 10:
            nombres.append(nombre)

        time.sleep(0.1)  # Pequeña pausa para ser amable con la API ❤️

    print(f"Pokémon encontrados (muestra): {', '.join(nombres)}")

def cadena_evolutiva_inicial():
    print("\n--- 2a. Cadena evolutiva de un inicial (Charmander) ---")
    especie = obtener_datos("pokemon-species/charmander")
    if not especie: return

    url_cadena = especie['evolution_chain']['url']
    cadena_data = requests.get(url_cadena).json()

    cadena = cadena_data['chain']
    evoluciones = []

    current_stage = cadena
    while current_stage:
        evoluciones.append(current_stage['species']['name'])
        if current_stage['evolves_to']:
            # Asumimos una línea simple para el inicial, tomamos el primero
            current_stage = current_stage['evolves_to'][0]
        else:
            current_stage = None

    print(f"Cadena evolutiva: {' -> '.join(evoluciones)}")


def electricos_sin_evolucion():
    print("\n--- 2b. Pokémon eléctricos sin evolución (Muestra) ---")
    data_electrico = obtener_datos("type/electric")
    sin_evo = []

    muestra = data_electrico['pokemon'][:15]

    for entry in muestra:
        nombre = entry['pokemon']['name']
        p_id = obtener_id_desde_url(entry['pokemon']['url'])

        # Obtenemos especie
        especie = obtener_datos(f"pokemon-species/{p_id}")
        if not especie: continue

        # Lógica: Si no evoluciona DE nadie y no evoluciona A nadie.
        # Pero la forma más segura es ver la cadena completa.
        url_cadena = especie['evolution_chain']['url']
        cadena_data = requests.get(url_cadena).json()
        chain = cadena_data['chain']

        if not chain['evolves_to']:
            sin_evo.append(nombre)

        time.sleep(0.1)

    print(f"Eléctricos sin evolución encontrados (en la muestra): {', '.join(sin_evo)}")

def mayor_ataque_johto():
    print("\n--- 3a. Mayor ataque base en Johto ---")
    # IDs de Johto: 152 a 251
    max_attack = -1
    max_pokemon = ""

    rango_demo = range(152, 162)
    print(f"Analizando rango ID {rango_demo.start}-{rango_demo.stop - 1}...")

    for p_id in rango_demo:
        p_data = obtener_datos(f"pokemon/{p_id}")
        if not p_data: continue

        for stat in p_data['stats']:
            if stat['stat']['name'] == 'attack':
                valor = stat['base_stat']
                if valor > max_attack:
                    max_attack = valor
                    max_pokemon = p_data['name']

    print(f"Mayor ataque en el rango analizado: {max_pokemon} ({max_attack})")


def mas_rapido_no_legendario():
    print("\n--- 3b. Pokémon más rápido no legendario (Kanto) ---")
    max_speed = -1
    fastest_mon = ""

    for p_id in range(1, 20):
        # 1. Chequear si es legendario (endpoint species)
        especie = obtener_datos(f"pokemon-species/{p_id}")
        if especie['is_legendary'] or especie['is_mythical']:
            continue

        # 2. Si no es legendario, ver velocidad (endpoint pokemon)
        p_data = obtener_datos(f"pokemon/{p_id}")
        for stat in p_data['stats']:
            if stat['stat']['name'] == 'speed':
                valor = stat['base_stat']
                if valor > max_speed:
                    max_speed = valor
                    fastest_mon = p_data['name']

    print(f"Más rápido no legendario (en muestra 1-20): {fastest_mon} ({max_speed})")

def habitat_comun_planta():
    print("\n--- 4a. Hábitat más común entre tipo Planta ---")
    data_planta = obtener_datos("type/grass")
    habitats = {}

    # Muestra de 15 pokémon
    for entry in data_planta['pokemon'][:15]:
        p_id = obtener_id_desde_url(entry['pokemon']['url'])
        especie = obtener_datos(f"pokemon-species/{p_id}")

        if especie and especie['habitat']:
            h_nombre = especie['habitat']['name']
            habitats[h_nombre] = habitats.get(h_nombre, 0) + 1

    if habitats:
        mas_comun = max(habitats, key=habitats.get)
        print(f"Hábitat más común (en muestra): {mas_comun} ({habitats[mas_comun]} veces)")
    else:
        print("No se encontraron datos de hábitat.")


def menor_peso():
    print("\n--- 4b. Pokémon con menor peso (Muestra) ---")
    # Revisamos los primeros 10 ID
    min_weight = float('inf')
    lightest_mon = ""

    for p_id in range(1, 11):
        data = obtener_datos(f"pokemon/{p_id}")
        if data:
            peso = data['weight']
            if peso < min_weight:
                min_weight = peso
                lightest_mon = data['name']

    print(f"Menor peso (en muestra 1-10): {lightest_mon} ({min_weight})")

if __name__ == "__main__":
    print("Iniciando análisis de PokeAPI...")
    contar_fuego_kanto()
    nombres_agua_altura_mayor_10()
    cadena_evolutiva_inicial()
    electricos_sin_evolucion()
    mayor_ataque_johto()
    mas_rapido_no_legendario()
    habitat_comun_planta()
    menor_peso()
    print("\nAnálisis completado.")