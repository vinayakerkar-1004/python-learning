# Taking input from the user
# input() always returns STRING → so we convert to integer using int()
a = int(input("Enter your age : "))

# ---------------- Conditional Statement ----------------
# if-else is used when there are only TWO possible conditions

# If condition is TRUE → if block runs
if(a >= 18):
    print("You are above the age of consent\nGood for you")

# If condition is FALSE → else block runs
else:
    print("You are below the age of consent")

# This line always runs (outside condition)
print("End of Program")