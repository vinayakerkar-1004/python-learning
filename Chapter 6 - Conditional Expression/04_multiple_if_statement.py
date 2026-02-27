# Taking user input
# input() returns string → convert to integer using int()
a = int(input("Enter your age : "))


# ---------------- If statement no : 1 ----------------
# This is an independent if condition
# It checks whether the number is EVEN

# % (modulus) gives remainder
# Even number → remainder 0 when divided by 2
if(a % 2 == 0):
    print("a is even")
# End of If statement no : 1


# ---------------- If statement no : 2 ----------------
# This is a SEPARATE decision block
# It checks age category

if(a >= 18):
    print("You are above the age of consent\nGood for you")

elif(a < 0):
    print("You are entering an invalid age")

elif(a == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")
# End of If statement no : 2


# This line always executes
print("End of Program")