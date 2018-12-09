# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = input(" Please enter a word, so that this programme can determine if it is a palindrome or not \n")
word = str(word)  # Ensuring that the entered word is a string

reverseWord =word[::-1]  #reverseing the word

print ("The word backwords is "+reverseWord)
if (word == reverseWord):
    print ("This word is a palindrome")
else:
    print ("This word is not a palindrome")


print ("\n")

#Using For loops
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')
