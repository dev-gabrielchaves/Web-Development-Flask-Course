# This is how you define a function
def hello():
    print('Hello') # Each time you call the function, program will read the body and this will come up

hello() # To actually run the function, you gotta call it and put the brackets next

# You can't call a function before you define it

# hellofriend() -> This won't work

# def hellofriend():
#     print('Hello Friend!')

# When we talk about functions there's something called 'scope'
friends = ['Matteo', 'João']

def add_friend():
    friend = input('Add Friend:')
    
    # Here I'm on the function scope, so friends will be a new variable in this case
    # friends = friends + [friend] -> This won't work 'cause I'm defining a variable and calling it on the same line
    
    # But if I just call without defining a new variable, the program you search for this...
    # variable in a 'before scope'
    friends.append(friend) # This will work

add_friend()

print(friends)

# Functions can receive parameters as you know
def hey_person(name):
    return f'Hey {name}!'

print(hey_person('Gabriel'))