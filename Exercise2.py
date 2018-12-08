#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?


randomNum = 0
randomNum = int(input("Please Enter a random number."))

modrandomNum = randomNum % 2   #modulus is the remainder, for even numbers/2, there will be no remainder, for odd numbers there is a remainder 

if modrandomNum == 0:
    print ("You have chosen an even number")
else:
    print ("You have chosen an odd number")

#Extras:

#If the number is a multiple of 4, print out a different message.

mod4 = randomNum % 4
if mod4 == 0:
    print (str(randomNum)+" is divisible by 4")
else: 
    print (str(randomNum)+" is not divisble by 4")

#Ask the user for two numbers: one number to check 
# (call it num) and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

num = int(input(" Please enter a number"))
check = int(input(" Please enter another number to check"))

divide = num % check

if divide == 0:
    print (str(check)+ " divides into "+str(num)+" perfectly")
else:
     print(str(check)+" does not divide into "+str(num)+ " prefectly")