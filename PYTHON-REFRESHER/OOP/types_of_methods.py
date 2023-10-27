class ClassTest:

    # Instace methods are the most used
    # They receive 'self' as the first parameter
    def instance_method(self):
        return(f'Called instace_method of {self}')
    
    @classmethod # Use it when you want to work with the class, or factories
    def class_method(cls):
        return(f'Called class_method of {cls}')
    
    @staticmethod # Use it when it makes sense to have the function on the class scope by some reason
    def static_method():
        return('Called static_method')
    
test = ClassTest()

# We always call instace methods through the object, or instace of the Class
print(test.instance_method()) # Output -> Called instace_method of <__main__.ClassTest object at 0x00000215F8404550> *To change representation use __str__ or __repr__ methods

# We should call class methods by it's class
print(ClassTest.class_method()) # Output -> Called class_method of <class '__main__.ClassTest'>

# Static methods are regular functions that are inside of a class scope because for the...
# developer it makes sense to have that function there
# You can run them by the class or the instance
print(ClassTest.static_method()) # Output -> Called static_method

# Let's see how and why we should use class methods

class Book:
    
    # Below I defined a class variable, usually we should call them all uppercase
    TYPE = ['hardcover', 'paperback']

    def __init__(self, title, type, weight) -> None:
        self.title = title
        self.type = type
        self.weight = weight
    
    def __repr__(self) -> str: # Defining representation of the object
        return f'<Book("{self.title}","{self.type}","{self.weight}")>'
    
    @classmethod # This method will allow us to instaciate a object through this method
    def hardcovered(cls, title, page_weight):
        return cls(title, cls.TYPE[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, title, page_weight):
        return cls(title, cls.TYPE[1], page_weight)
    
book_1 = Book('Harry Potter', 'hardcover', 1500)

print(book_1)

# Instaciating the object through the class method
hardcovered_book = Book.hardcovered('Lord of the Rings', 1700)

print(hardcovered_book)

# Instaciating the object through the class method
paperback_book = Book.paperback('Marvel vs DC', 700)

print(paperback_book)