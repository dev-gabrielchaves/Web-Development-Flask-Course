# Methods that has this structure __method__, are called magic methods
# Such as: __init__, __str__, __repr__, etc.
# But what are __str__ and __repr__?
# To examplify let's create a class

class Person: # Class Person

    def __init__(self, name: str, age: int) -> None: # Built in method
        # It's attributes
        self.name = name
        self.age = age
    
    # The __str__ and __repr__ methods are very similar, they just a different purpose
    # The __str__ is used to show users a nicer view of the object
    # The __repr__ is used to create a representation of the object to the developer
    # Let's see how it works
    def __str__(self) -> str:
        return f'{self.name} is {self.age} year(s) old!' # Thinking on the users

    def __repr__(self) -> str:
        return f'<Person("{self.name}", "{self.age}")>' # Thinking on the developers

bob = Person('Bob', 34)

print(bob.age) # Output -> 34

bob.__init__('Bob', 35) # Calling the __init__ method allows you to change objects attributes

print(bob.age) # Output -> 35

# By default this will call the __str__method
# You can use the three differents ways on the following to show our object representation to the users
print(bob) # Output -> Bob is 35 year(s) old!
print(str(bob))
print(bob.__str__())

# Calling the method __repr__
print(bob.__repr__()) # Output -> <Person("Bob", "35")>

# When not defined these methods, by default if calling the object, it will show where it is located on the memory