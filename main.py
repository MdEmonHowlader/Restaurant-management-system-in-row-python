from users import Admin, Customer, Employee
from menu import Menu
from resturent import Restaurant
from order import Order
from fooditem import Fooditem

mama_res = Restaurant("Kacchi Bhai")
def print_centered(text, width=100):
    print(text.center(width))
def line_separator(width=100):
    print('*' *width)
def Customere_menu():
    name= input("Enter your Name: ")
    email= input("Enter your Email: ")
    phone= input("Enter your Phone: ")
    address= input("Enter your Address")
    customer = Customer(name=name, email=email, phone=phone, address=address)
    while True:
        line_separator()
        print_centered("Welcome {costumer.name}")
        line_separator()
        print_centered("1. Show Menu")
        print_centered("2. Order Food")
        print_centered("3. Show Cart")
        print_centered("4. Checkout")
        print_centered("5. Exit")
        choice = input("Enter your choice: ")
        if choice == 1:
            customer.show_menu(mama_res.menu)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            customer.order_food(mama_res.menu, item_name, quantity)
        elif choice ==3:
            customer.show_cart()
        elif choice == 4:
            customer.checkout()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")
def admin_menu():
    name =input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = int(input("Enter your Phone: "))
    address = input("Enter your Address")
    admin =Admin(name=name, email=email, phone=phone, address=address)
    while True:
        line_separator()
        print_centered("Welcome {admin.name}")
        print_centered("1. Add Food Item")
        print_centered("2. Add New Employee")
        print_centered("3. View Employees")
        print_centered("4. View Items")
        print_centered("5. Delete Item")
        print_centered("6. Exit")   
        choice = int(input("Enter Your Choice: "))
        if(choice == 1):
            name= input("Enter Food Name: ")
            price=int(input("Enter Food Price: "))
            quantity =int(input("Enter Food Quantity: "))
            item= Fooditem(name=name, price=price, quantity=quantity)
            admin.add_food_item(mama_res, item)
        elif choice == 2:
            name = input("Enter Employee Name: ")
            phone = int(input("Enter Employee Phone: "))
            email = input("Enter Employee Email: ")
            address = input("Enter Employee Address: ")
            designation = input("Enter Employee Designation: ")
            age = int(input("Enter Employee Age: "))
            salary = int(input("Enter Employee Salary: "))
            employee= Employee(name=name, email=email, phone=phone, address=address, designation=designation, age=age, salary=salary)
            admin.add_employee(mama_res, employee)
        elif choice == 3:
            admin.view_employee(mama_res)
        elif choice ==4:
            admin.view_menu(mama_res)
        elif choice==5:
            item_name= input("Enter Item Name: ")
            admin.remove_food(mama_res, item_name)
        elif choice ==6:
            break
        else:
            print("Invalid Choice")
while True:
    line_separator()
    print_centered("*******Welcome to Mama's Restaurant****")
    line_separator()
    print_centered("1. Customer")
    print_centered("2. Admin")
    print_centered("3. Exit")
    line_separator()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Customere_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
                       
            
            
    
