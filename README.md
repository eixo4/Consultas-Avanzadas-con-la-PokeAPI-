# 📊 Análisis de Datos Pokémon con PokeAPI

Este proyecto es una herramienta de línea de comandos escrita en **Python** que interactúa con la [PokeAPI](https://pokeapi.co/) para extraer, filtrar y analizar datos sobre el universo Pokémon.

El script responde a preguntas específicas sobre tipos, evoluciones, estadísticas de combate y hábitats mediante consultas HTTP.

## 🚀 Funcionalidades

El script realiza las siguientes tareas de análisis:

* **🔥 Clasificación por Tipos:**
    * Cuenta cuántos Pokémon de tipo *Fuego* hay en Kanto (Gen 1).
    * Lista Pokémon de tipo *Agua* con una altura superior a 10.

* **🧬 Cadenas Evolutivas:**
    * Reconstruye la cadena evolutiva completa de un Pokémon inicial (ej. Charmander).
    * Identifica Pokémon de tipo *Eléctrico* que no tienen evoluciones.

* **⚔️ Estadísticas de Batalla:**
    * Encuentra el Pokémon con mayor ataque en la región de Johto.
    * Busca el Pokémon más rápido (no legendario).

* **🌍 Datos Curiosos:**
    * Determina el hábitat más común para los Pokémon de tipo *Planta*.
    * Encuentra el Pokémon más liviano de una muestra.

## 📋 Requisitos Previos

* Python 3.x
* Conexión a Internet (para consultar la API).
* Librería `requests`.

### Instalación de dependencias

```bash
pip install requests
````

## ▶️ Cómo Ejecutar

Simplemente ejecuta el script principal desde tu terminal:

```bash
python analisis_pokemon.py
```

## 📝 Ejemplo de Salida

A continuación se muestra una ejecución real del script, donde se observa el análisis de muestras de datos:

```text
Iniciando análisis de PokeAPI...

--- 1a. Pokémon tipo Fuego en Kanto ---
Total de Pokémon tipo Fuego en Kanto: 12

--- 1b. Pokémon tipo Agua con altura > 10 ---
Revisando una muestra de 20 Pokémon de tipo agua...
Pokémon encontrados (muestra): blastoise, golduck, poliwrath, tentacruel, slowpoke, slowbro, seel, dewgong, cloyster, kingler, seadra

--- 2a. Cadena evolutiva de un inicial (Charmander) ---
Cadena evolutiva: charmander -> charmeleon -> charizard

--- 2b. Pokémon eléctricos sin evolución (Muestra) ---
Eléctricos sin evolución encontrados (en la muestra): zapdos

--- 3a. Mayor ataque base en Johto ---
Analizando rango ID 152-161...
Mayor ataque en el rango analizado: feraligatr (105)

--- 3b. Pokémon más rápido no legendario (Kanto) ---
Más rápido no legendario (en muestra 1-20): pidgeot (101)

--- 4a. Hábitat más común entre tipo Planta ---
Hábitat más común (en muestra): grassland (8 veces)

--- 4b. Pokémon con menor peso (Muestra) ---
Menor peso (en muestra 1-10): caterpie (29)

Análisis completado.
```

Capturas:
<img width="1630" height="863" alt="image" src="https://github.com/user-attachments/assets/d6498a9a-9024-498a-b9da-6d0f4eb0e1f6" />
<img width="1087" height="182" alt="image" src="https://github.com/user-attachments/assets/32f5f1bb-e70b-4342-82cf-bf15014a8dda" />



## ⚠️ Nota sobre el Rendimiento

Para evitar saturar la API y garantizar una ejecución rápida durante las pruebas, algunas funciones analizan solo una **muestra** de los datos (por ejemplo, los primeros 20 registros).

Para realizar un análisis sobre la totalidad de los Pokémon existentes, puedes modificar los rangos en el código fuente (ej. eliminar `[:20]`).
