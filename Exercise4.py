# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input(" Please enter a number"))
divlist = []

#create a list ranging from 1 to a number+1
listRange = list(range(1,num+1))

for element in listRange:
    if num % element == 0 :
        divlist.append(element)
print (divlist)
