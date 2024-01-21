list = []
templist = []
str = input('Enter a string: ')

for i in range(len(str)):
    templist.append(str[i])
    if len(templist) == 3:
        list.append(templist)
        templist = []
else:
    list.append(templist)

print(list)