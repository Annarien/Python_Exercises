## Character Input
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them 
# that tells them the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number and printing out that many 
# copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)


import datetime 
now = datetime.datetime.now()

#def CharacterMethod():
name = ""
age = 0
difference100 = 0
currentyear = 0
year100 = 0
num = 0

name = input ("What is your name?")
age = int(input("What is your age?"))
difference100 = 100 - age

print(name+" you will be 100 years in ",(now.year+difference100))
sentence = name + " you will be 100  years old in "+ str((now.year+difference100))+"\n" # ending sentence with "\n" to add a new line after it

num = int(input(" Please enter a random number from 0 to 20.")) #asaking user to enter a random number
if (num > 0 and num < 20):
    print(num*(sentence))               # printing the sentence the amount of times given by the random number
  
else:
    print("Please try again")
