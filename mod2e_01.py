str = input("Enter a string: ")

for i in range(len(str) - 1, -1, -1):
    print(str[i], end='')