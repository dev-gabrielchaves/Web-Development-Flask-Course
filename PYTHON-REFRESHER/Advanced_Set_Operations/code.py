# Defining our sets
friends = {'Matteo', 'João', 'Alfonso'}
abroad = {'Alfonso'}

# Get the difference of sets
local_friends = friends.difference(abroad)

print(local_friends) # -> {'Matteo', 'João'}

# Defining our set
local = {'Matteo', 'João'}

# Unify both sets
all_friends = local.union(abroad)

print(all_friends)

# There's more methods to use in sets, just keep that in mind!