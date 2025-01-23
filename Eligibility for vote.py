age=int(input('Enter Your Age:'))
if age>0:
    print('Valid Input')
    if age>=18:
        print('Eligible For Vote')
    else:
        print('Not Eligible For Vote')
else:
    print('Invalid Age')