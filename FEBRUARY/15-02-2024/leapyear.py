n=int(input('Enter the year: '))
if n%4==0 and n%100!=0:
    print('Leap year')
elif n%400==0:
    print('Leap year')

else:
    print('Not a leap year')
