# By default every function returns -> None
def add(x, y):
    print(x + y)

add(1, 2) # Output -> 3, calling function that executs the function print and returns None

result = add(3, 5) # Output -> 8, calling function that executs the function print and returns None assigning it to the variable result

print(result) # Output -> None

def add_three(x, y, z):
    return x + y + z

add_three(1, 2, 3) # No output

result = add_three(1, 2, 3) # No output, but as it returns the sum of all three numbers it will assign that value to the variable result

print(result) # Output -> 6

# OBS.: When the return is executed it automatically breaks the function and returns the value