"""
OPERATOR OVERLOADING:
Consider that we have two objects which are a physical representation of a class (user-defined data type)
 and we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know
 how to add two objects. So we define a method for an operator and that process is called operator overloading.
To perform operator overloading, Python provides some special function or magic function that is automatically
invoked when it is associated with that particular operator. For example, when we use + operator, the magic method
 __add__ is automatically invoked in which the operation for + operator is defined.
"""
from oops_log import get_logger

lg = get_logger(name="(Polymorphism_Operator_over_loading)", file_name="oops_log.log")


class Addition:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


if __name__ == '__main__':
    ob1 = Addition(1)
    ob2 = Addition(2)
    ob3 = Addition("Shivaraj")
    ob4 = Addition("Gowda")

lg.debug(ob1 + ob2)
lg.debug(ob3 + ob4)

"""
3
ShivarajGowda
"""
