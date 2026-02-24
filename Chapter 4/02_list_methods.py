# Creating a list
# A list is an ordered, mutable (changeable) collection in Python
friends = ["Vinay", "Fantom", 1004, True, "Akerkar", "Family"]

# print() -> Displays the entire list
print(friends)


# ---------------- List Methods ----------------

# list.append(value)
# Adds a new element at the END of the list
friends.append("Python")
print(friends)


# Creating another list
list1 = [4, 12, 10, 12, 1004, 12]

# list.sort()
# Sorts the list in ascending order (modifies original list)
list1.sort()
print(list1)

# list.reverse()
# Reverses the order of elements in the list
list1.reverse()
print(list1)

# list.insert(index, value)
# Inserts a value at a specific position
# Example: insert 121223 at index 2
list1.insert(2, 121223)
print(list1)

# list.pop(index)
# Removes and RETURNS the element at the given index
value = list1.pop(2)
print(value)
print(list1)

# list.sort(reverse=True)
# Sorts the list in descending order
list1.sort(reverse=True)
print(list1)

# list.remove(value)
# Removes the FIRST occurrence of the specified value
list1.remove(12)

# print the updated list
print(list1)


# ---------------- Built-in Functions ----------------

# type(variable)
# Returns the data type of the variable
print(type(friends))
print(type(list1))

# len(list)
# Returns total number of elements in the list
print(len(friends))