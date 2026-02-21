name = "vinay akerkar"

# Returns the total number of characters in the string (including spaces)
# Output: 13
print(len(name))

# Checks if the string starts with "VI". (False, because strings are case-sensitive)
print(name.startswith("VI"))

# Checks if the string starts with "vi". (True)
print(name.startswith("vi"))

# Checks if the string ends with "in". (False, the string ends with "r")
print(name.endswith("in"))

# Checks if the string ends with "ay". (False, the string ends with "akerkar")
print(name.endswith("ay"))

# Capitalizes the first character of the string and makes the rest lowercase
# Output: "Vinay akerkar"
print(name.capitalize())

# Searches for the substring "akerkar" and returns the index where it starts
# Output: 6 (v=0, i=1, n=2, a=3, y=4, space=5, a=6)
print(name.find("akerkar"))

# Counts how many times the letter "k" appears in the string
# Output: 2
print(name.count("k"))

# Returns a new string where "vinay" is replaced with "fantom"
# Output: "fantom akerkar"
print(name.replace("vinay", "fantom"))