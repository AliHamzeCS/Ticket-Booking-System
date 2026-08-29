import json
import os


CUSTOMERS_FILE = 'customers.json'


# Load Customers
def Load_Customers():

    if not os.path.exists(CUSTOMERS_FILE):
        return {}

    try:
        with open(CUSTOMERS_FILE, 'r') as file:
            Customers = json.load(file)

            New_Customers = {}

            for key, value in Customers.items():
                New_Customers[int(key)] = value

            return New_Customers

    except json.JSONDecodeError:
        return {}
    
# Dump Customers
def Dump_Customers(Customers):

    with open(CUSTOMERS_FILE, 'w') as file:
        json.dump(Customers, file, indent=4)
        
# Add Customers
def Add_Customers(customers, customers_id, customers_data):
    
    customers[customers_id] = customers_data
    Dump_Customers(customers)