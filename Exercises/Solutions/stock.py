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
