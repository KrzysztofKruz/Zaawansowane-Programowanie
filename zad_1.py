class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks)/len(self.marks) > 50:
            return True
        else:
            return False


Student1 = Student("Tomasz", [56, 76, 42, 99, 99])

Student2 = Student("Krzysztof", [12, 43, 65, 12, 11])

Student1.is_passed()

Student2.is_passed()
