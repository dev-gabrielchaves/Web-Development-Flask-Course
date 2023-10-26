# Dictionary comprehension is kind the same of list comprehension

users = [
    {
        'name':'Gabriel',
        'age': 24, 
        'password': '12345'
    },
    {
        'name':'João',
        'age': 18, 
        'password': '54321'
    },
    {
        'name':'Carla',
        'age': 44, 
        'password': 'idk123'
    }
]

# Creating a mapping dictionary with all user's information with a key name
users_mapping = {user['name']:user for user in users}

# This will show all the information of Gabriel
print(users_mapping['Gabriel']) # Output -> {'name': 'Gabriel', 'age': 24, 'password': '12345'}

# Without Dict. Comp.
for user in users:
    if user['name'] == 'Gabriel':
        print(user)