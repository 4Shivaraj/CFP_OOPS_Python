"""
METHOD OVERLOADING:
Methods in Python can be called with zero, one, or more parameters.
This process of calling the same method in different ways is called method overloading
python does not support method overloading by default. But there are different ways
to achieve method overloading in Python.
"""

from oops_log import get_logger

lg = get_logger(name="(Polymorphism_Method_over_loading)", file_name="oops_log.log")

"""
def addition(a, b):
    c = a + b
    print(c)


def addition(a, b, c):
    d = a + b + c
    print(d)


# the below line shows an error
# addition(4, 5)

# This line will call the second product method
addition(3, 7, 5)
"""

# The desired way to achieve the method overloading, by using multiple dispatch decorator
# Multiple Dispatch Decorator Can be installed by: pip3 install multipledispatch

from multipledispatch import dispatch


class Calculator:
    @dispatch(int, int)
    def product(first, second):
        result = first * second
        lg.debug(result)

    @dispatch(int, int, int)
    def product(first, second, third):
        result = first * second * third
        lg.debug(result)

    @dispatch(float, float, float)
    def product(first, second, third):
        result = first * second * third
        lg.debug(result)

"""
16
12
17.204
"""


product_obj = Calculator()
product_obj.product(2, 8)
product_obj.product(2, 3, 2)
product_obj.product(2.2, 3.4, 2.3)
