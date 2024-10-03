"""
This application uses the requests library to query the Pokemon API.
The API requires the requests library, which is specified in the requirements.txt file.
The application makes a GET request to the URL https://pokeapi.co/api/v2/pokemon and prints the results to the console.
"""

import requests


def fetch_pokemon_data(pokemon_url: str) -> dict:
    """
    Fetches Pokémon data from the API.

    Args:
        pokemon_url (str): The URL of the Pokémon API endpoint.

    Returns:
        dict: The Pokémon data in JSON format.
    """
    try:
        response = requests.get(pokemon_url, timeout=10)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching Pokémon data: {e}")
        return None


def print_pokemon_data(pokemon_data: dict) -> None:
    """
    Prints the Pokémon data.

    Args:
        pokemon_data (dict): The Pokémon data in JSON format.
    """
    if pokemon_data:
        print("Successfully fetched data from the API:")
        print(pokemon_data)
    else:
        print("Error fetching data from the API")


pokemon_url = "https://pokeapi.co/api/v2/pokemon/ditto"
pokemon_data = fetch_pokemon_data(pokemon_url)
print_pokemon_data(pokemon_data)
