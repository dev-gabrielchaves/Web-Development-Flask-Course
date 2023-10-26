# Content related to classes 28, 29 and some youtube videos as well

# What * does is to unpack the parameters given and transform them into a tuple
def multiply(*nums): # It doesn't need to be called 'args'
    print(type(nums)) # Output -> <class 'tuple'>
    total = 1
    for num in nums:
        total *= num
    return total

result = multiply(1, 2, 3) # Passing multiple values to the function multiply

print(result)

# What ** does is to unpack the parameters given and transform them into a dictionary
def print_street(**kwargs):
    print(type(kwargs)) # Output -> <class 'dict'>
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_street(street='Gilberto Rodrigues', number=186, zipcode='59190-000', city='Canguaretama')