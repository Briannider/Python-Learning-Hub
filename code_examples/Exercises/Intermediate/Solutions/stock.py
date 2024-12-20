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


def add_video_game(name, price, quantity, category, platforms):
    """Adds a new video game to the stock with the given name, price, quantity, and category."""
    new_game = {
        "price": price,
        "quantity": quantity,
        "category": category,
        "platforms": platforms,
    }
    stock[name] = new_game


def show_stock():
    """Prints the full stock."""
    for video_game, details in stock.items():
        print(f"Name: {video_game}")
        print(f"Price: {details['price']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Category: {details['category']}")
        print(f"Platforms: {', '.join(details['platforms'])}")
        print()


def check_product(name):
    """Checks if a video game exists in the stock."""
    if name in stock:
        print(f"Name: {name}")
        print(f"Price: {stock[name]['price']}")
        print(f"Quantity: {stock[name]['quantity']}")
        print(f"Category: {stock[name]['category']}")
        print(f"Platforms: {', '.join(stock[name]['platforms'])}")
    else:
        print(f"{name} doesn't exist in the stock.")


def remove_video_game(name):
    """Removes a video game from the stock if it exists."""
    if name in stock:
        del stock[name]
        print(f"Removed {name} from the stock.")
    else:
        print(f"{name} doesn't exist in the stock.")


def modify_stock(name, quantity):
    """Modifies the stock quantity of a video game."""
    if name in stock:
        stock[name]["quantity"] += quantity
        print(f"Updated stock quantity for {name}: {stock[name]['quantity']}")
    else:
        print(f"{name} doesn't exist in the stock.")


def update_video_game(name, price, quantity, category):
    """Updates the stock of the video game with the given name."""
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


def remove_product(stock):
    """Removes a product from the stock."""
    name = input("Enter the name of the product you want to remove: ")
    if name in stock:
        del stock[name]
        print(f"Removed {name} from the stock.")
    else:
        print(f"{name} doesn't exist in the stock.")


def low_stock():
    """Prints video games with low quantity."""
    for video_game in stock:
        if stock[video_game]["quantity"] < 5:
            print(f"{video_game} is low in stock.")


def show_menu():
    """Displays the main menu and handles user input."""
    while True:
        # Print the main menu options
        print("========== MAIN MENU (Product Management) ==========")
        print("Option 1: Add a new product")
        print("Option 2: Check product data")
        print("Option 3: Modify Stock quantity")
        print("Option 4: Remove a product")
        print("Option 5: Full product list")
        print("Option 6: List of products with low quantity")
        print("Option 7: Exit")
        print("===================================================")

        # Get the user's choice
        option = int(input("Choose an Option: "))

        # Call the corresponding function based on the user's choice
        if option == 1:
            name = input("Enter the name of the game: ")
            price = int(input("Enter the price of the game: "))
            quantity = int(input("Enter the quantity of the game: "))
            category = input("Enter the category of the game: ")
            platforms = input(
                "Enter the platforms of the game (separated by commas): "
            ).split(",")
            add_video_game(name, price, quantity, category, platforms)
        elif option == 2:
            game_name = input("Enter the name of the game your searchin for: ")
            check_product(game_name)
        elif option == 3:
            modify_stock(stock)
        elif option == 4:
            remove_product(stock)
            # elif option == 5:
            show_stock()
        elif option == 6:
            low_stock()
        elif option == 7:
            break  # Exit the menu loop
        else:
            print("Invalid option. Please choose a valid option.")


show_menu()
