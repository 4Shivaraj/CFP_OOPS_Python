"""
POLYMORPHISM :
            Poly means many and morphism means forms, when you are the same entity
(+ operator in this case) but behaviour changes in different circumstances
"""
from oops_log import get_logger

lg = get_logger(name="(Polymorphism)", file_name="oops_log.log")


def add(a, b):
    return a + b


if __name__ == '__main__':

    lg.debug(add(5, 6))
    lg.debug(add("shiv", "raj"))
    lg.debug(add([1, 2, 3, 34], [34, 55, 66]))

"""
11
shivraj
[1, 2, 3, 34, 34, 55, 66]
"""
