#W.a.p to read a number, if it is not a zero then only check given is +ve number
#or -ve number otherwise display message as 'Given Number is Zero'

n=int(input('Enter any number:'))
if n!=0:
    if n>0:
        print('Given Number is +ve Number')
    else:
        print('Given Number is -ve Number')
else:
    print('Given Number is Zero')