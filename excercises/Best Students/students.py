class Student:
    def __init__(self, name, last_name, grades):
        self.name = name
        self.lastname = last_name
        if 0 < grades <= 10:
            self.grades = grades
        else:
            raise ValueError("How could you even get a different grade? Be real!")

    def __str__(self):
        return "Name: {} - Last Name {} - Grade {}".format(
            self.name, self.last_name, self.grades
        )
