from abc import ABC
from order import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.orders = []
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    def create_order(self, customer: Customer, order: Order):
        customer.orders.append(order)
class Employee(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    def take_order(self, customer: Customer, order: Order):
        customer.orders.append(order)
    def deliver_order(self, customer: Customer, order: Order):
        customer.orders.remove(order)