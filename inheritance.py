"""
INHERITANCE:it allows you to inherit property(all variables functions and method) of parent class to child class
if there is a classes and there are variables inside the class,and if we need to re-utilise functions without rewriting
code that is achievable in Inheritance
"""

from oops_log import get_logger

lg = get_logger(name="(Inheritance)", file_name="oops_log.log")


class Company:
    company_website = "https://bridgelabz.com/"
    name = "bridge_labz"

    def contact_details(self):
        lg.info("contact us at", self.company_website)


class Datascience(Company):
    def __init__(self):
        self.year_of_establishment = 2015

    def est_details(self):
        lg.debug("{0} company was established in {1}".format(self.name, self.year_of_establishment))


if __name__ == '__main__':
    course_obj = Datascience()
    course_obj.est_details()