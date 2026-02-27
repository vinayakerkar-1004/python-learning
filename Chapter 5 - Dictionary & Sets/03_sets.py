# Creating a set
# A set is an unordered collection of UNIQUE elements
# Duplicate values are automatically removed

s = {1, 5, 32, 54, 5, 5, 5}

# type() -> shows the data type
print(type(s))

# Printing the set
# Duplicate 5 will appear only once
print(s)


# ---------------- Important Concept ----------------

# Creating {} creates an EMPTY DICTIONARY, not a set
s = {}
print(type(s))   # <class 'dict'>


# To create an empty set, use set()
s = set()
print(type(s))   # <class 'set'>

# NOTE:
# Never use s = {} for empty set
# {} -> dictionary
# set() -> empty set
