# Taking user input
a = int(input("Enter your age : "))

# ---------------- If-Elif-Else Ladder ----------------
# Used when there are MULTIPLE conditions to check

# Condition 1
if(a >= 18):
    print("You are above the age of consent\nGood for you")

# Condition 2 (checked only if first condition is False)
elif(a < 0):
    print("You are entering an invalid age")

# Condition 3
elif(a == 0):
    print("You are entering 0 which is not a valid age")

# Runs when NONE of the above conditions are True
else:
    print("You are below the age of consent")

# Always executed
print("End of Program")