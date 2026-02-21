# The variable 'a' contains several escape sequences:
# \\ -> Renders a single backslash
# \n -> Inserts a new line (line break)
# \t -> Inserts a horizontal tab (extra spacing)
# \' or \" -> Allows you to use quotes inside a string defined by those same quotes
a = "Vinay is a \\good boy\nbut 'not' a\tbad \"boy\""

# When printed, Python processes those escape sequences into their visual formatting
print(a)