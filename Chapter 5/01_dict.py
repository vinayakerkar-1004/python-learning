d = {} # Empty dictionary
print(type(d))

dict = {
    "name": "Vinay",
    "age": 23,
    "marks": 90.99,
    "is_adult": True,
    "subjects": ["python", "java"],   # list as value
    "topics": ("dict", "set"),        # tuple as value
    10: "Fantom"                      # numeric key is also allowed
}

print(dict, type(dict))
# Accessing value using key
# Returns value associated with the key
print(dict["name"])