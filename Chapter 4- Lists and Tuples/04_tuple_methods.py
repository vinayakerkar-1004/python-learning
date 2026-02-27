# Creating a tuple with multiple data types
# A tuple is an ordered, immutable collection in Python
a = (1, 4, 12, 10, 12, 1004, 12, "Vinay", False, True, 69.69)

# print() -> Displays the entire tuple
print(a)


# ---------------- Tuple Methods ----------------

# tuple.count(value)
# Returns how many times a specific value appears inside the tuple
no = a.count(12)
print(no)


# tuple.index(value)
# Returns the index (position) of the FIRST occurrence of the given value
# Indexing starts from 0
i = a.index(12)
print(i)


# ---------------- Tuple Operations ----------------

# Creating two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation (+)
# Combines two tuples into a single new tuple
concatenated = tuple1 + tuple2
print(concatenated)


# Repetition (*)
# Repeats the elements of the tuple n number of times
repeated = tuple1 * 3
print(repeated)


# ---------------- Membership Operators ----------------

# 'in' operator
# Checks if an element exists inside the tuple (returns True/False)
print(2 in tuple1)   # True → 2 exists in tuple1
print(4 in tuple1)   # False → 4 does not exist in tuple1


# ---------------- Built-in Functions ----------------

# len(tuple)
# Returns the total number of elements in the tuple
print(len(tuple1))