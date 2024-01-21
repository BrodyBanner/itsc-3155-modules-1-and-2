rownum = input('Enter a row num from 1 to 5: ')
colnum = input('Enter a col num from 1 to 5: ')

for i in range(1,6):
    for j in range(1,6):
        if i == int(rownum) and j == int(colnum):
            print('1 ', end='')
        else:
            print('0 ', end='')
    else: 
        print()