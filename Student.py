class Student:
    def __init__(self, name=None, house=None):
        # Initialize a new Student with a name and house
        self.name = name
        self.house = house

    def __str__(self):
        # Return a string representation of the Student object
        return f"Name: {self.name} | House: {self.house}"
    
    def __eq__(self, new_student):
        # Check if two Student objects are equal by comparing their names
        if isinstance(new_student, Student):
            return self.name == new_student.name
        return False
