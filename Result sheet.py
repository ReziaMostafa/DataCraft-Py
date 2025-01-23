# w.a.p to read 3 subject marks, then find total, avg and grade.
#avg>70%      Grade-A
#avg b/w 60-70  Grade-B
#avg b/w 50-60  Grade-C
#otherwise      Grade-D



s1 =int(input('Enter Sub-1 Marks:'))
s2 =int(input('Enter Sub-2 Marks:'))
s3 =int(input('Enter Sub-3 Marks'))

tot =s1+s2+s3
avg =tot/3
print('Total is:',tot)
print('Average is:',avg)
if avg>70:
   print('Grade-A')
elif 60<=avg<70:
    print('Grade-B')
elif 50<=avg<60:
    print('Grade-C')
else:
    print('Grade-D')



