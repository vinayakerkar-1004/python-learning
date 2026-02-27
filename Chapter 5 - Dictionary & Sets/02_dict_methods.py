#A dictionary in Python is a mutable data structure that stores data in key-value pairs, where each key is unique and used to access its corresponding value.

# Creating a dictionary
# A dictionary stores data in KEY : VALUE pairs
# Keys must be unique and immutable (string, number, tuple)
# Values can be of any data type

dict = {
    "name": "Vinay",
    "age": 23,
    "marks": 90.99,
    "is_adult": True,
    "subjects": ["python", "java"],   # list as value
    "topics": ("dict", "set"),        # tuple as value
    10: "Fantom"                      # numeric key is also allowed
}

# print() -> Displays the entire dictionary
print(dict)


# Accessing value using key
# Returns value associated with the key
print(dict["name"])


# ---------------- Dictionary Methods ----------------

# dict.items()
# Returns all key-value pairs as tuples inside a view object
print(dict.items())


# dict.keys()
# Returns a list-like view of all keys
print(dict.keys())


# dict.values()
# Returns a list-like view of all values
print(dict.values())


# dict.update({key:value})
# Updates existing keys OR adds new key-value pairs
# Here: age updated and new key "Akerkar" added
dict.update({"age": 24, "Akerkar": 100})
print(dict)


# dict.get(key)
# Safely returns the value of the key
# If key does NOT exist → returns None (NO error)
print(dict.get("name"))
print(dict.get("name1"))  # returns None


# Direct indexing with []
# If key does NOT exist → program crashes (KeyError)
print(dict["name2"])  # Raises error