class Student:

    def __init__(self, name, age) -> None: # Built in method
        self.name = name
        self.age = age
    
    def description(self) -> str: # Methods are functions inside of a class
        return f'My name is {self.name}, and I have {self.age} years old!'

student_1 = Student('Mario', 25) # Instaciating class

print(student_1.description()) # Calling it's method through the object