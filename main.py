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
            customer.order_food(mama_res.menu)
