#Take a list, say for example this one:

 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

i = 0

for element in a:
     if ( a[i]<5):
         print(a[i])
     i =i+1

#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
b =[1, 1, 2, 3] 
print(b)
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

num = int(input(" Please enter a number"))
j = 0
for element in a:
    if (a[j] < num):
        print (a[j])
    j=j+1

