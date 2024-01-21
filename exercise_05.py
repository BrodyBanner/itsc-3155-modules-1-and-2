list1 = []
list2 = []
clist = []

for i in range(5):
    list1.append(int(input('Enter a number for the first list: ')))

for i in range(5):
    list2.append(int(input('Enter a number for the second list: ')))

print('First List: ' + str(list1))
print('Second List: ' + str(list2))

for i in range(5):
    for j in range(5):
        if list1[i] == list2[j]:
            clist.append(list1[i])

#The line of code below was taken from the online source W3Schools. It converts the list to a dictionary object, which cannot
#contain duplicates, and then converts it back into a list object.
#https://www.w3schools.com/python/python_howto_remove_duplicates.asp
clist = list(dict.fromkeys(clist))

print('Common List: ' + str(clist))