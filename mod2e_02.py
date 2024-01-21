str = input("Enter a string: ")
lower = ""
upper = ""

for i in range(len(str)):
    if (str[i] == " "):
        pass
    elif (str[i] == str[i].capitalize()):
        upper += str[i]
    else:
        lower += str[i]

print(lower + upper)