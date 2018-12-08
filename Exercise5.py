#Take two lists, say for example these two:

 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:

#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)  

import random

a = random.sample(range(1,30),10)   # random numbers from 1 to 30, with a size of 10
b = random.sample(range(1,50),20)   # random numbers from 1 to 50, with a size of 20

print (a)
print (b)
myList = []

for num in a:  #if  a number in a, is equal to b then add the number myList and then print it
    if num in b:
        myList.append(num)
print (myList)

