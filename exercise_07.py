list = []
evlist = []
temp = input('Enter a number or QUIT to quit: ')

while temp != 'QUIT':
    temp = input('Enter a number or QUIT to quit: ')
    if temp == 'QUIT':
        break
    list.append(int(temp))

print('All Nums: ' + str(list))

for i in list:
    if i % 2 == 0:
        evlist.append(list[i - 1])

print('Even Nums: ' + str(evlist))