# As we know functions can receive parameters and do something with them
# But in Python we can also define default values for the functions parameters

def sum_two_numbers(x, y=5): # Here, by default, if none second parameter is added when calling the function, y default's value is gonna be 5
    return x + y

print(sum_two_numbers(5)) # Output -> 10, It won't come up an error 'cause we defined y's default value
print(sum_two_numbers(5, 10)) # Output -> 15

# def sum_three_numbers(x, y=5, z): -> We cannot do something like this, for it to work z needs to have an default value as well
def sum_three_numbers(x, y=5, z=3):
    return x + y + z

# Something to remenber is to always assign the default value within the function, so don't do something like the following
default_d = 2

def sum_four_numbers(a, b, c, d = default_d):
    return a + b + c + d

print(sum_four_numbers(1, 2, 3)) # Output -> 8

default_d = 5 # Even tough I do this, it won't be assign another value to d, 'cause it is done when you create the function

print(sum_four_numbers(1, 2, 3)) # Output -> 8