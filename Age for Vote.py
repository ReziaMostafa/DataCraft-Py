#W.a.p to read age of a person, if it is +ve number then only check person is
# Eligible for Vote or not otherwise display message as 'Invalid Age'

age=int(input('Enter Your Age:'))
if age>0:
    print('Valid Input')
    if age>=18:
        print('Eligible For Vote')
    else:
        print('Not Eligible For Vote')
else:
    print('Invalid Input')