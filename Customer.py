from random import randint
from BookingsHistory import Load_Bookings
import CustomersHistory
from Utils import decorator_func

Bookings = Load_Bookings()
customers = CustomersHistory.Load_Customers()



# Add Customer
@decorator_func('Add Customer')
def add_customer():
    
    cust_name = input("Enter Customer Name : ")
    cust_phone = input("Enter Customer Phone : ")
    cust_id = randint(999, 10000)

    while True:
        if cust_id not in customers:
            customers[cust_id] = {
                'Customer Name': cust_name,
                'Customer Phone': cust_phone
            }
            CustomersHistory.Dump_Customers(customers)
            break

        else:
            cust_id = randint(999, 10000)

    print('✅ Data saved')


# Show Customers
@decorator_func('Show Customers')
def show_customers():
    shapes = ['👤', '📱']

    if not customers:
        print("❌ No customers found.")
        return

    for ID in customers:
        print("=" * 25)
        print("👤 CUSTOMER", end='\n\n')
        print(f"🆔 Customer ID : {ID}")

        for shape, key in zip(shapes, customers[ID]):
            print(f"{shape} {key} : {customers[ID][key]}")

        print()
        print("=" * 25)


# Update Customers
@decorator_func('Update Customers')
def update_customers():
    shapes = ['👤', '📱']

    try:
        cust_id = int(input('Enter Customer ID : '))

    except ValueError:
        print('❌ Enter only Customer ID.')
        return

    found = False

    if cust_id in customers:
        found = True

    if not found:
        print("❌ Customer ID not found.")
        return

    print("=" * 25)
    print("👤 CUSTOMER", end='\n\n')
    print(f"🆔 Customer ID : {cust_id}")

    for shape, key in zip(shapes, customers[cust_id]):
        print(f"{shape} {key} : {customers[cust_id][key]}")

    print()
    print("=" * 25, end='\n\n')

    print('What do you want to modify?\n')
    print('1. Customer Name')
    print('2. Customer Phone')
    print('3. Back\n')

    try:
        choice = int(input('Choice : '))

    except ValueError:
        print('❌ Choice must be a number.')
        return

    if choice == 1:
        new_name = input('Enter the new name : ')

        customers[cust_id]['Customer Name'] = new_name
        CustomersHistory.Dump_Customers(customers)

        print("=" * 25)
        print("👤 CUSTOMER", end='\n\n')
        print(f"🆔 Customer ID : {cust_id}")

        for shape, key in zip(shapes, customers[cust_id]):
            print(f"{shape} {key} : {customers[cust_id][key]}")

        print()
        print("=" * 25, end='\n\n')

    elif choice == 2:
        new_phone_number = input('Enter the new phone number : ')

        customers[cust_id]['Customer Phone'] = new_phone_number
        CustomersHistory.Dump_Customers(customers)

        print("=" * 25)
        print("👤 CUSTOMER", end='\n\n')
        print(f"🆔 Customer ID : {cust_id}")

        for shape, key in zip(shapes, customers[cust_id]):
            print(f"{shape} {key} : {customers[cust_id][key]}")

        print()
        print("=" * 25, end='\n\n')

    elif choice == 3:
        return

    else:
        print('❌ Invalid choice.')
        return


# Delete Customer
@decorator_func('Delete Customer')
def delete_customer():
    shapes = ['👤', '📱']

    try:
        cust_id = int(input('Enter Customer ID : '))

    except ValueError:
        print("❌ Customer ID must be a number.")
        return

    found = False

    if cust_id in customers:
        found = True

    if not found:
        print("❌ Customer ID not found.")
        return

    print("=" * 25)
    print("👤 CUSTOMER", end='\n\n')
    print(f"🆔 Customer ID : {cust_id}")

    for shape, key in zip(shapes, customers[cust_id]):
        print(f"{shape} {key} : {customers[cust_id][key]}")

    print()
    print("=" * 25, end='\n\n')

    while True:
        choice = input('Delete this customer? (Y/N) : ').lower()

        if choice == 'y':
            del customers[cust_id]
            CustomersHistory.Dump_Customers(customers)
            print('✅ Customer is deleted')
            break

        elif choice == 'n':
            print('❌ Deletion cancelled.')
            break

        else:
            print('⚠️ Please enter only Y or N')
            
# Customer Bookings       
@decorator_func('Customer Bookings') 
def Customer_Bookings():
    Bookings = Load_Bookings()
    shapes = ['👤', '📱']
    icons = ['🎫','🎬','⏰','💺','👤','📱','💰']
    
    try:
        cust_id = int(input('Enter Customer ID : '))
    
    except ValueError:
        print("❌ Customer ID must be a number.")
        return
    
    found = False
    
    if cust_id in customers:
        found = True
    
    if not found:
        print("❌ Customer ID not found.")
        return
    
    print("=" * 25)
    print("👤 CUSTOMER", end='\n\n')
    print(f"🆔 Customer ID : {cust_id}")
    
    for shape, key in zip(shapes, customers[cust_id]):
        print(f"{shape} {key} : {customers[cust_id][key]}")
    
    print()
    print("=" * 25, end='\n\n')
    
    index = 1
    found_bookings = False
    for ID in Bookings :
        if cust_id == Bookings[ID].get("Customer ID"):
            found_bookings = True
            print(f"🎟️ Booking #{index}")
            index += 1
            for icon , Key in zip(icons , Bookings[ID]):
                print(f"{icon} {Key} : {Bookings[ID][Key]}")
                
    if not found_bookings :
        print("⚠️ This customer has no bookings.")
        
        