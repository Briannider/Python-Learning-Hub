# Exercise: Inventory Management System
Imagine you're designing a small system to manage the inventory of a video game store. In this system, each video game has a name, a price, a stock quantity, and a category. You need to implement several functions to efficiently manage this inventory.

### Step 1: Define the Inventory Dictionary

Create an `inventory` dictionary where each key is the name of a video game, and its value is another dictionary with the following details:

- `"price"`: price of the video game (float)
- `"quantity"`: quantity in stock (int)
- `"category"`: category of the video game (str) (e.g., "action," "adventure," "sports")

### Step 2: Functions to Manage Inventory

1. **Add a New Video Game**  
   Create a function `add_video_game(name, price, quantity, category)` that receives the details of a new video game and adds it to the inventory. If the video game already exists, update its quantity.

2. **Remove a Video Game**  
   Implement the function `remove_video_game(name)` to remove a video game from the inventory. If the game doesn’t exist, display a message indicating it wasn’t found.

3. **Search Video Games by Category**  
   Define the function `search_by_category(category)` to return a list of all video games that belong to a specific category.

4. **Get Total Inventory Value**  
   Create the function `total_inventory_value()` that calculates the total value of all video games in stock (price multiplied by quantity).

5. **List Low-Stock Video Games**  
   Implement `low_stock_video_games(limit)` to get a list of all video games with a stock quantity below the specified limit.
