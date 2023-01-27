## String Variables in Python
# var_name = "Brother"
# var1 = "Sister"
# PI = 22 / 7

## Integer Variables
# age = 21
# age += 1
# print("Your age is: " + str(age))  # String Concatenation

## Floating Variables
# height = 1.75
# print(f"Your height is: {height}")

## Boolean Variables
# human = True
# print(f"are you a human? {human}")

## Multiple assignments
# name, age, attractive = "Nelson", 27, True  # example 1
# print(f"my name is {name}, I  am {age} years old \nAm I attractive: {attractive}")

# nelson = esther = emmanuel = frank = 600  # example 2

## string methods in python
# name = "Nelson Udeme"
# print(name.find("N"))  # shows the index of the string in the variable
# print(name.capitalize())
# print(name.lower())
# print(name.upper())
# print(name.isalpha())
# print(name.isdigit())
# print(name.count("e"))
# print(name.replace("Udeme", "udeme-Abasi"))
# print(name * 2)


# import time
#
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!🎉🎆")


### Nested loops in Python
# rows = int(input("How many rows?:"))
# columns = int(input("How many columns?:"))
#
# symbol = input("Enter a symbol to use")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

###----------------------------------------------------------------------------
# while True:
#     name = input('Enter your name: ')
#     if name != "":
#         break

##------------------------------------------------------------------------
# phone_number = "+234-812-657-9885"
#
# for i in phone_number:
#     if i == "-" or i == "+":
#         continue
#     print(i, end="")

##-------------------------------------------------------------------------
##Python Lists

# food = ['garri', 'fufu', 'pizza', 'beans', 'rice']
# food[1] = "golden morn"
#
# food.append("ice-cream")
# food.pop()
# food.remove("golden morn")
# food.insert(0, "fufu")
# food.sort()
# print(food, end="\n")
# print(food.count('garri'))
### 2 Dimensional list--------------------------------------------------------------------

### tuples--------------------------------------------------------------------------------

### Sets----------------------------------------------------------------------------------
# utensils = {'fork', 'spoon', 'knives'}
# dishes = {'bowl', 'plate', 'cup'}

### Dictionaries
# countries = {"Nigeria": "FCT",
#              "Mali": "Bamako",
#              "Sierra Leone": "Freetown",
#              "Cameroon": "Yaounde"}
# print(countries["Nigeria"])
# print(countries.get("germany"))
# print(countries.values(), countries.keys())
#
# for k, v in countries.items():
#     print(k, v)
#
# countries.update({'Kenya': 'Nairobi'})
# countries.pop('Kenya')
# print(countries.items())


##-------------------------PYTHON FUNCTIONS--------------------------------------------------------------
# def hello(name):
#     print(f"Hello {name}!")
#     print('Have a nice day')


# --------------*args for function packing
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return print(sum)
#
#
# add(1, 2, 3, 4)


# --------------**kwargs for function packing

# def greeting(**kwargs):
#     print('Hello! ', end="")
#     for (k, v) in kwargs.items():
#         print(v, end="")
#
#
# greeting(first_name='Nelson', last_name='Udeme-Abasi')

### string formatting-------------------------------------------------------------

# num = 13475389
# name = "Nelson"
#
# print(f'The number is {num}')
# print(f'The name is {name:10}')
# print(f'The name is {name:>10}')  # to align right in display margin
# print(f'The name is {name:^10}')  # to centralise string display margin
# print(f'The number is {num:.2f}')  # to display as 2 sig. fig.
# print(f'The number is {num:b}')  # to display as binary
# print(f'The number is {num:,}')  # to display as comma separated
# print(f'The number is {num:o}')  # to display as octadecimal
# print(f'The number is {num:E}')  # to display as scientific
# print(f'The number is {num:X}')  # to display as hexadecimal


### --------------------------------Random numbers and items--------------------------------------------
# import random
#
# x = random.randint(1, 10)
# y = random.random()
# z = random.choice(['a', 'b', 'c'])
# xx = ['heart', 'jack', 'spade', 'diamonds', 'king', 'queen', 'ace']
# random.shuffle(xx)
#
# print(x)
# print(y)
# print(z)
# print(xx)


### --------------------------------Exception Handling in Python-------------------------------------------
# try:
#     num = int(input('Pls input numerator: '))
#     dem = int(input('Pls input denominator: '))
#     res = num / dem
#     print(res)
# except ZeroDivisionError:
#     print('∞')
# except Exception:
#     print('Something went wrong, pls make sure you put numbers')
# else:  ### this block is for when all has failed(exceptions you couldn't capture)
#     print(result)
# finally:  ### this code block will run regardless of whether an exception applied or not
#     print('This is the finally block of the try and exception block')


### ---------------------------Handling files with python in your PC-------------------------------------------

# import os
#
# path = 'C:\\Users\\Nelson\\My PC\\Desktop\\UGHE_Logo_Design'
# if os.path.exists(path):
#     print('This file exists')
#     if os.path.isfile(path):
#         print('It is a file')
#     elif os.path.isdir(path):
#         print('It is a directory')
# else:
#     print('File does not exist!')

## Reading the contents of your file line by line
# with open('file.txt') as file: #there's a default 'r' arguement for reading the file in th open function
#     print(file.read())

## Writing into a new file using python
# with open('test.txt', 'w') as file:  # we included 'w' arguement to show we intend to create a file, 'a' is to append
#     file.write("Hello again\nMy name is Nelson Udeme\n"
#                "This is just another example of python basics\n"
#                "I'm enjoying this!")
#
# import shutil
#
# shutil.copyfile('')

# help('modules') #gives a list of modules/packages in python


### --------------------------------Rock, Paper, Scissors Game------------------------------------------------
import random

while True:
    choices = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Pls select rock, paper or scissors: ').lower()

    if player == comp_choice:
        print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nIts a tie!')
    elif player == 'rock':
        if comp_choice == 'paper':
            print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nYou Lose!')
        if comp_choice == 'scissors':
            print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nYou win!')
    elif player == 'scissors':
        if comp_choice == 'rock':
            print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nYou Lose!')
        if comp_choice == 'paper':
            print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nYou win!')
    elif player == 'paper':
        if comp_choice == 'scissors':
            print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nYou Lose!')
        if comp_choice == 'rock':
            print(f'Computer: {comp_choice}\nPlayer Choice: {player}\nYou win!')

    play_again = input('Would you like to play again? (y/n):').lower()
    if play_again != "y":
        break
print('Bye!')
