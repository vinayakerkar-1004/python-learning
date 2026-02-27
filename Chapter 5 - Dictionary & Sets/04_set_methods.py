# Creating a set
# A set is an unordered collection of UNIQUE elements
# Duplicate values are automatically removed

s = {1, 5, 32, 54, 5, 5, 5, "Vinay"}

# print() -> displays set elements
# type() -> shows the datatype (set)
print(s, type(s))


# ---------------- Set Methods ----------------

# set.add(value)
# Adds a new element to the set
# If the element already exists, nothing changes (no duplicates allowed)
s.add(566)
print(s, type(s))


# len(set)
# Returns the total number of UNIQUE elements in the set
print(len(s))


# set.remove(value)
# Removes the specified element
# If the element does not exist → raises KeyError
s.remove(1)
print(s)


# set.clear()
# Removes ALL elements from the set (set becomes empty)
s.clear()
print(s)