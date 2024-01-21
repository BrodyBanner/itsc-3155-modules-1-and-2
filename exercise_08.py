list = []
onelist = []

for i in range(1,11):
    list.append(int(input('Enter number ' + str(i) + ': ')))

for i in range(0,10):
    if list.count(list[i]) == 1:
        onelist.append(list[i])

print('Original List: ' + str(list))
print('Nums that appear once: ' + str(onelist))