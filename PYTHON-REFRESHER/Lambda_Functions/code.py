# Lambda functions, are one-line functions that doesn't have to have a name assign to perform
# Lambda functions are focused on the input and output, not performing actions
# Let's go for some examples

# That's the structure of a lambda function: lambda (parameters) : (what it returns)
add = lambda x, y: x + y # I've assigned a name but it isn't necessary
print(add(2, 3)) # Output -> 5

# Performing lambda function on a single lign without assigning it to a variable
print((lambda x, y, z : x + y + z)(1, 2, 3)) # Output -> 6