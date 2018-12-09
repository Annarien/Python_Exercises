#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evenList = []
oddList = []
i = 0


for i in a:
    modofa = a[i] % 2
    if (modofa > 0):
        oddList.append(a[i])
    else:
        evenList.append(a[i])
i=i+1

print (evenList)
print (oddList)