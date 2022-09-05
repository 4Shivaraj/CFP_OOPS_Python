from oops_log import get_logger

lg = get_logger(name="(Multiple_Inheritance)", file_name="oops_log.log")


class Student1:
    def __init__(self):
        self.name = 'Shivaraj'
        self.age = 19

    def get_name(self):
        return self.name


class Student2:
    def __init__(self):
        self.name = 'Cheluvesha'
        self.id = '15'

    def get_name(self):
        return self.name


class Students(Student1, Student2):
    def __init__(self):
        Student2.__init__(self)
        Student1.__init__(self)

    def get_name(self):
        lg.info(self.name)
        return self.name


student_obj = Students()
print(student_obj.get_name())

"""
Shivaraj
"""
