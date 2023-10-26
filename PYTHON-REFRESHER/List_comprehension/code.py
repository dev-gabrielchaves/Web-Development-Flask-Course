# Lists comprehension it's a way to make the developer's life easier

# Let's make a scenario to show how useful list comprehension really is
# So we have a list o numbers and we want to multiply by 2 each element
# Without list comprehension we would do it like the following
numbers = [1, 2, 3, 4, 5]
numbers_by_2 = []

for number in numbers:
    numbers_by_2.append(number * 2)

print(numbers_by_2)

# With list comprehension it would be like the following
# The basic structure of a list comprehension is like this...
# variable = [what we want for iteration]
# In the case bellow we want "number * 2"
# And our iteration would be "number in numbers"
list_comprehension_number_by_2 = [number * 2 for number in numbers ]
print(list_comprehension_number_by_2)

# Let's make another case where we use a if statement
# I want to print the name of the friends that starts with a "S"
friends = ['João', 'Sara', 'samantha', 'Matteo', 'Georgia']

# I know that every name should start with capital case, but that's just to illustrate
# So let's go
# Here we kepr the same structure that was said before, but now we added an if statement to the end
# And that's exactly how you do it
friends_with_s = [friend for friend in friends if friend.startswith('S') or friend.startswith('s')]
# variable = [what we want for iteration if condition]

print(friends_with_s) # Output -> ['Sara', 'samantha']

# The sequence of logic in this case is 
# First - Iterate
# Second - Check condition
# Third - Add element
# So for example in this case you will see that the lists won't contain 'Samantha' even tough I'm capitalazing 
friends_with_s = [friend.capitalize() for friend in friends if friend.startswith('S')]

print(friends_with_s) # Output -> ['Sara']

# Bellow I'm just gonna exercise this topic

student_grade = {
    'Pedro': 50,
    'Gabriel': 90,
    'João': 70,
    'Paulo': 58
}

list_aproved_students = [f'{student} was aproved' for student, grade in student_grade.items() if grade >= 60]

print(list_aproved_students)