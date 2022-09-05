from oops_log import get_logger

lg = get_logger(name="(Multi_level_Inheritance)", file_name="oops_log.log")


class Person:

    def __init__(self, details_dict):
        self.name = details_dict.get("name")
        self.city = details_dict.get("city")


class Students(Person):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.roll_no = details_dict.get("roll_no")
        self.year = details_dict.get("year")


class Civil(Students):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.course_fees = details_dict.get("course_fees")


class Electronics(Students):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.course_fees = details_dict.get("course_fees")


if __name__ == '__main__':
    student_one = Civil({"name": "Shivaraj", "dob": 1998, "roll_no": "297", "city": "Bangalore", "year": 2022,
                         "course_fees": 130000})
    student_two = Electronics({"name": "Cheluvesha", "dob": 1997, "roll_no": "257", "city": "Bangalore", "year": 2022,
                               "course_fees": 100000})
    lg.debug(student_one.name)
    lg.debug(student_two.name)

"""
Shivaraj
Cheluvesha
"""