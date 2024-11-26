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
        # Send a GET request to the API, with a timeout of 10 seconds
        response = requests.get(pokemon_url, timeout=10)
        # Raise an exception for 4xx or 5xx status codes
        response.raise_for_status()
        # Return the JSON data
        return response.json()
    except requests.RequestException as e:
        # Print an error message if there's an exception
        print(f"Error fetching Pokémon data: {e}")
        # Return None to indicate an error
        return None


def print_pokemon_data(pokemon_data: dict) -> None:
    """
    Prints the Pokémon data.

    Args:
        pokemon_data (dict): The Pokémon data in JSON format.
    """
    if pokemon_data:
        # Print a success message if we got data
        print("Successfully fetched data from the API:")
        # Print the data
        print(pokemon_data)
    else:
        # Print an error message if we didn't get data
        print("Error fetching data from the API")


if __name__ == "__main__":
    # Define the URL of the Pokémon API endpoint
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/ditto"
    # Fetch the data
    pokemon_data = fetch_pokemon_data(pokemon_url)
    # Print the data
    print_pokemon_data(pokemon_data)
