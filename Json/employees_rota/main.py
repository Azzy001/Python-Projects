import json
import random

# --------------------

def load_employees():
    try:
        with open("json/employees_rota/employees.json", "r") as file:
            employees = json.load(file)
        employees = [employee["firstname"] for employee in employees.values()]
        
    except FileNotFoundError:
        return []
    
    return list(employees)

# --------------------

def view_employees(employees):
    print(employees)

# --------------------

def add_employee(employees):
    employee_to_add = input("Enter name of employee you want to add: ")
    employees.append(employee_to_add)
    print(f"Employee {employee_to_add} has been added successfully.")

# --------------------

def remove_employee(employees):
    employee_to_remove = input("Enter name of employee you want to remove: ")
    if employee_to_remove in employees:
        employees.remove(employee_to_remove)
        print(f"{employee_to_remove} removed from the list.")
    else:
        print(f"{employee_to_remove} not found in the list.")

# --------------------
        
def generate_rota(employees):
    services = ["ServiceNow", "Jira", "PagerDuty", "DSST Channel & Email"]
    assign_employees_to_roles = {service: [] for service in services}
    random.shuffle(employees)

    for service in services:
        if employees:
            employee = employees.pop()
            assign_employees_to_roles[service].append(employee)
    return assign_employees_to_roles

# --------------------

def display_options():
    employees = load_employees()
    while True:
        try:
            choice = int(input("Select options:\n"+
                               "1. view employee list.\n"+
                               "2. add to employee list.\n"+
                               "3. remove from employee list.\n"+
                               "4. generate rota.\n"+
                               "5. exit program.\n"))
            if choice == 1:
                view_employees(employees)
            elif choice == 2:
                add_employee(employees)
            elif choice == 3:
                remove_employee(employees)
            elif choice == 4:
                generate_rota(employees)
            elif choice == 5:
                print("Goodbye.")
                break

        except ValueError:
            print("Incorrect option, try again.")

# --------------------

display_options()

"""
november - march - block 2 module
block 3 - march (current) until june
block 1 - September 2025

completing block 3 now
complete block 1 in sept 25
block 2 module in november 2024
"""
