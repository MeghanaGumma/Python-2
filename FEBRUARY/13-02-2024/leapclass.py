class sol:
    def leap(self,n):
        if n%4==0 and n%100!=0:
            return True
        elif n%400==0:
            return True
        else:
            return False
        
n=int(input('Enter the year: '))
obj=sol()
if obj.leap(n):
    print('Leap year')
else:
    print('Not a leap year')
    
    
