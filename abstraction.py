"""
ABSTRACTION:
            is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementation of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
"""

from abc import ABC, abstractmethod
from oops_log import get_logger

lg = get_logger(name="(Abstraction)", file_name="oops_log.log")


class Computation(ABC):

    @abstractmethod
    def check_attendance(self):
        """
        doc string
        """

    @abstractmethod
    def calculate_wage(self):
        ...  # pass


class Employee(Computation):
    def check_attendance(self):
        lg.debug("Employee is present")

    def calculate_wage(self):
        lg.debug("Employee wage")


if __name__ == '__main__':
    obj = Employee()
    obj.check_attendance()
    obj.calculate_wage()

"""
Employee is present
Employee wage
"""
