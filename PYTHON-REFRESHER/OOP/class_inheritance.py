# Creating class Person, that will be the mother class
class Person:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Student(Person): # Student inherits Person

    def __init__(self, name, age, *grades) -> None:
        super().__init__(name, age) # Getting attributes from mother class
        self.grades = grades # This is a tuple, don't forget it
    
    def average_grade(self): # Calculating average
        return sum(self.grades)/len(self.grades)

    def __str__(self) -> str:
        return f'{self.name} has {self.age} years old, and has an average grade of: {self.average_grade()}!'

gabriel = Student('Gabriel', 24, 90, 90, 90, 100, 75)

# print(gabriel)

# Another example, just to remind it
# This example was the one showed on the video
class Device:
    
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def disconnect(self):
        if self.connected == False:
            return print('Device already disconnected!')
        else:
            self.connected = False
            status = self.connected
            return status
    
    def connect(self):
        if self.connected:
            return print('Device already connected!')
        else:
            self.connected = True
            status = self.connected
            return status
    
    def __str__(self) -> str:
        
        if self.connected:
            return f'The {self.name} is connected by {self.connected_by}, and the connection is stablished!'
        else:
            return f'The {self.name} is connected by {self.connected_by}, and the connection is not stablished!'

class Printer(Device):

    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.pages_left = capacity
    
    def do_print(self, pages):
        self.pages_left = self.pages_left - pages
        return f'{self.name} printed {pages} pages, and there is {self.pages_left} page(s) left!'

printer = Device('Printer', 'USB')
print(printer)

xerox = Printer('Xerox', 'USB', 500)
print(xerox.do_print(20))
# I already understand how it works, so I won't spend so much time explaining again