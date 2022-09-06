"""
METHOD OVERRIDING:
Using method overriding polymorphism allows us to define methods in the child class that
have the same name as the methods in the parent class. This process of re-implementing the
inherited method in the child class is known as Method Overriding.

we have a vehicle class as a parent and a ‘Car’ and ‘Truck’ as its subclass.
But each vehicle can have a different seating capacity, speed, etc., so we can have the same
instance method name in each class but with a different implementation.
Using this code can be extended and easily maintained over time.
"""
from oops_log import get_logger

lg = get_logger(name="(Polymorphism_Method_over_riding)", file_name="oops_log.log")

class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        lg.debug('Vehicle max speed is 150')

    def change_gear(self):
        lg.debug('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        lg.debug('Car max speed is 240')

    def change_gear(self):
        lg.debug('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()

"""
Car max speed is 240
Car change 7 gear
Vehicle max speed is 150
Vehicle change 6 gear
"""