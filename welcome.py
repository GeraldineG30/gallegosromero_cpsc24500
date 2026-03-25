from datetime import datetime

# FOR NAME INPUT AND DECORATION
name = input("Enter your name: ")
print ("\n" + "=D  " * 30)
print (f" Welcome {name}!")
print ("\n" + ":D  " * 30)

# FOR DATETIME MODULE
time_now = datetime.now()
print (f"The Current Date and Time: {time_now}")

# DIFFERENT TYPES OF VARIABLES
middle_name = "Sara" # str
age = 23             # int
height = 5.3         # float

# EXTRA F-STRINGS
print (f"{middle_name} is {age} years old")
print (f"{middle_name} height is {height} ft")

