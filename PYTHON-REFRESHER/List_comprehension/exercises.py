# List comprehension problems in python
# Content taken from: https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = []
vowels = ['a', 'e', 'i', 'o', 'u']

for fruit in fruits:
    counter = 0
    for letter in fruit:
        if letter in vowels:
            counter += 1
    if counter > 2:
        fruits_with_more_than_two_vowels.append(fruit)

print(fruits_with_more_than_two_vowels)

# Using list comprehension
fruits_with_more_than_two_vowels = [f for f in fruits if len([True for v in f if v in ['a', 'e', 'i', 'o', 'u']]) > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_two_vowels = [f for f in fruits if len([True for v in f if v in ['a', 'e', 'i', 'o', 'u']]) == 2]
print(fruits_with_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_characters = [f for f in fruits if len(f)>5]
print(fruits_with_more_than_five_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_five_characters = [f for f in fruits if len(f)==5]
print(fruits_with_five_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_characters = [f for f in fruits if len(f)<5]
print(fruits_with_less_than_five_characters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruits_number_of_characters = [len(f) for f in fruits]
print(fruits_number_of_characters)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [f for f in fruits if ('a' or 'A') in f]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [n for n in numbers if n%2==1]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [n for n in numbers if n%2==0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [n for n in numbers if n>0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [n for n in numbers if n<0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
# There ain't a function that can measure directly the length of a number, you must turn it into a string for this
list_of_numbers_with_two_or_more_numerals = [n for n in numbers if len(str(n))>2]
print(list_of_numbers_with_two_or_more_numerals)
    
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n**2 for n in numbers]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if (n%2==0) and n<0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
number_plus_five = [n+5 for n in numbers]
print(number_plus_five)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
from sympy import isprime
primes = [n for n in numbers if isprime(n)]
print(primes)