## Exercise: Managing a Nested Dictionary of Employee Records

You work at a tech company, and your task is to create a system to manage employee records using a nested dictionary. Each employee record includes their name, department, position, and a list of completed projects.

### Step 1: Create the Initial Dictionary

1. Create a dictionary called `employees` with the following structure:

   ```python
   employees = {
       "E001": {"name": "Alice", "department": "Engineering", "position": "Developer", "projects": ["Website", "App"]},
       "E002": {"name": "Bob", "department": "Marketing", "position": "Manager", "projects": ["Campaign A"]},
       "E003": {"name": "Carol", "department": "Engineering", "position": "Designer", "projects": []},
       "E004": {"name": "Dave", "department": "Sales", "position": "Salesperson", "projects": []}
   }
   ```

### Step 2: Define Functions for Managing Employees

2. Write functions to manage this dictionary as follows:

   - **`add_employee`**: Adds a new employee to the dictionary.
   - **`remove_employee`**: Removes an employee from the dictionary by their employee ID.
   - **`add_project`**: Adds a project to an employee’s project list.
   - **`list_projects_by_department`**: Lists all projects for employees in a specific department.

   Each function should have appropriate parameters and should handle cases where the employee or department does not exist.

### Step 3: Implement the Functions

Here are some function signatures and a description of each function:

1. **`add_employee(employees, emp_id, name, department, position)`**:
   - Adds a new employee to the `employees` dictionary.
   - If the employee ID already exists, return an error message.

2. **`remove_employee(employees, emp_id)`**:
   - Removes the employee with the given ID from the dictionary.
   - If the employee ID does not exist, return an error message.

3. **`add_project(employees, emp_id, project_name)`**:
   - Adds a new project to the specified employee’s project list.
   - If the employee ID does not exist, return an error message.

4. **`list_projects_by_department(employees, department)`**:
   - Returns a list of all projects for employees in a given department.
   - If the department does not exist or has no employees with projects, return an empty list.

### Step 4: Test Cases

Use the following test cases to ensure your functions work:

1. Add a new employee with ID `"E004"`.
2. Remove the employee with ID `"E003"`.
3. Add a project called `"SEO Optimization"` to the employee with ID `"E002"`.
4. List all projects in the "Engineering" department.

---

This exercise helps you practice using nested dictionaries, data manipulation in Python, and creating functions that can be extended or adapted for specific needs.