"""
You work at a tech company, and your task is to create a system to manage employee records using a nested dictionary. 
Each employee record includes their name, department, position, and a list of completed projects.
---------------------------------------------------------------------------------------------------------------------
   - `add_employee`: Adds a new employee to the dictionary.
   - `remove_employee`: Removes an employee from the dictionary by their employee ID.
   - `add_project`: Adds a project to an employee's project list.
   - `list_projects_by_department`: Lists all projects for employees in a specific department.
---------------------------------------------------------------------------------------------------------------------
"""

employees = {
    "E001": {
        "name": "Alice",
        "department": "Engineering",
        "position": "Developer",
        "projects": ["Website", "App"],
    },
    "E002": {
        "name": "Bob",
        "department": "Marketing",
        "position": "Manager",
        "projects": ["Campaign A"],
    },
    "E003": {
        "name": "Carol",
        "department": "Engineering",
        "position": "Designer",
        "projects": [],
    },
    "E004": {
        "name": "Dave",
        "department": "Sales",
        "position": "Salesperson",
        "projects": [],
    },
}


def add_employee(name, department, position, projects):
    print
