"""
A dictionary to store the video game stock.

The keys are the names of the video games and the values are dictionaries
with the following keys:

- price: an integer representing the price of the video game.
- quantity: an integer representing the quantity of the video game.
- category: a string representing the category of the video game.
- platforms: a list of strings representing the platforms on which the
  video game is available.
"""

stock = {
    "Minecraft": {
        "price": 40,
        "quantity": 6,
        "category": "Adventure",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
    "FIFA": {
        "price": 80,
        "quantity": 6,
        "category": "Sports",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
    "Dragon Ball Z": {
        "price": 100,
        "quantity": 6,
        "category": "Fighting",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
    "League Of Leguends": {
        "price": -100,
        "quantity": 6,
        "category": "Strategy",
        "platforms": ["PC"],
    },
    "COD": {
        "price": 100,
        "quantity": 6,
        "category": "Shooter",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
    "Overwatch": {
        "price": 80,
        "quantity": 6,
        "category": "Shooter",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
    "Apex Legends": {
        "price": 0,
        "quantity": 0,
        "category": "Shooter",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
    "Fortnite": {
        "price": 0,
        "quantity": 0,
        "category": "Shooter",
        "platforms": ["PC", "Xbox", "PlayStation"],
    },
}


def add_video_game(name, price, quantity, category):
    """
    Adds a new video game to the stock with the given name, price, quantity, and category.
    """
    new_game = {
        "price": price,
        "quantity": quantity,
        "category": category,
        "platforms": [],
    }
    stock[name] = new_game


def remove_video_game(name):
    """Removes a video game from the stock if it exists."""
    if name in stock:
        del stock[name]
        print(f"Removed {name} from the stock.")
    else:
        print(f"{name} doesn't exist in the stock.")


def update_video_game(name, price, quantity, category):
    """
    Updates the stock of the video game with the given name.

    It checks if the video game exists in the stock and prints a message
    accordingly.
    """
    if name in stock:
        updated_game = {
            "price": price,
            "quantity": quantity,
            "category": category,
            "platforms": [],
        }
        stock[name] = updated_game
    else:
        print(f"{name} doesn't exist in the stock.")
