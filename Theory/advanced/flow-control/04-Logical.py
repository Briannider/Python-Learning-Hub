"""
This script checks whether a vehicle can move forward based on certain conditions.

The conditions are:
- There must be no gas.
- The engine must be running.
- The driver's age must be greater than 17.
"""

# Define the status of gas availability
gas = False

# Define if the engine is currently running
engine_running = True

# Define the driver's age
age = 18

# Check if all conditions are met to move forward
if not gas and engine_running and age > 17:
    print("You can move forward")
