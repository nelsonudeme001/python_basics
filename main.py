# String Variables in Python
var_name = "Brother"
var1 = "Sister"
PI = 22 / 7

# Integer Variables
age = 21
age += 1
print("Your age is: " + str(age))  # String Concatenation

# Floating Variables
height = 1.75
print(f"Your height is: {height}")

# Boolean Variables
human = True
print(f"are you a human? {human}")

# Multiple assignments
name, age, attractive = "Nelson", 27, True  # example 1
print(f"my name is {name}, I  am {age} years old \nAm I attractive: {attractive}")

nelson = esther = emmanuel = frank = 600  # example 2

# string methods in python
name = "Nelson Udeme"
print(name.find("N"))  # shows the index of the string in the variable
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.isalpha())
print(name.isdigit())
print(name.count("e"))
print(name.replace("Udeme", "udeme-Abasi"))
print(name * 2)
