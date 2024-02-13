class employee:
    
    def getdata(self,eno,ename,des,sal,hra,da,ta):
        self.eno=eno
        self.ename=ename
        self.des=des
        self.sal=sal
        self.hra=hra
        self.da=da
        self.ta=ta
    def putdata(self):
        print('Employee no: ',self.eno)
        print('Employee name: ',self.ename)
        print('Employee designation: ',self.des)
        print('Basic salary: ',self.sal)
        print('House rent allowance: ',self.hra)
        print('Dearness allowance: ',self.da)
        print('Travel allowance: ',self.ta)
        netsal = self.sal + self.da + self.ta + self.hra
        if netsal>50000:
            tax=5/100*netsal
        elif netsal>35000:
            tax=3/100*netsal
        elif netsal>20000:
            tax=1/100*netsal
        else:
            tax=0
        print('Net salary: ',netsal)
        print('Tax: ',tax)

e=employee()
eno=int(input('Enter employee no: '))
ename=input('Enter employee name: ')
des=input('Enter designation: ')
sal=int(input('Enter basic salary: '))
hra=int(input('Enter house rent allowance: '))
da=int(input('Enter dearness allowance: '))
ta=int(input('Enter travel allowance: '))
e.getdata(eno,ename,des,sal,hra,da,ta)
e.putdata()

