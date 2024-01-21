num = input('Enter a number: ')
x = 1
numlist = []

while x <= int(num):
    temp = input('Enter number ' + str(x) + ': ')
    numlist.append(float(temp))
    x += 1

print('List: ' + str(numlist))
print('Average: ' + str(sum(numlist)/int(num)))