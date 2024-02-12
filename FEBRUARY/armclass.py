class sol:
    def armstrong(self,n):
        temp=n
        sum=0
        while n!=0:
            r=n%10
            sum+=r*r*r
            n//=10
        if temp==sum:
            return True
        else:
            return False
n=int(input())
obj=sol()
if obj.armstrong(n):
    print('Armstrong')
else:
    print('Not Armstrong')
