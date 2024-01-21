list = []
onestr = ''

for i in range(5):
    list.append(input('Enter a word: '))

for i in range(5):
    onestr += (str(list[i]) + ' ')

print('Words: ' + str(list))
print('One String: ' + onestr)