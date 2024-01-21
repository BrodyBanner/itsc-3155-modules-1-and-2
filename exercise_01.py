grade = input('Enter a grade from 0 to 100: ')

if int(grade) < 60:
    print('Your grade is F')
elif int(grade) < 70:
    print('Your grade is D')
elif int(grade) < 80:
    print('Your grade is C')
elif int(grade) < 90:
    print('Your grade is B')
else:
    print('Your grade is A')