s={}
n=int(input('Enter no. of students: '))
for i in range(n):
    l=[]
    htno=int(input('Enter htno: '))
    sname=input('Enter Name: ')
    s1=int(input('Enter Maths marks: '))
    s2=int(input('Enter Accountancy marks: '))
    s3=int(input('Enter Computer Science marks: '))
    s4=int(input('Enter Economics marks: '))
    s5=int(input('Enter Business Studies marks: '))
    l.append(sname)
    l.append(s1)
    l.append(s2)
    l.append(s3)
    l.append(s4)
    l.append(s5)
    s[htno]=l
print(s)  
'''
hno=int(input("Enter htno:"))
print("Name of the student: ",s[hno][0])
total=s[hno][1]+s[hno][2]+s[hno][3]+s[hno][4]+s[hno][5]
avg=total//5
print('Total: ',total)
print('Percentage: ',avg,'%')
if avg>60:
    print('Pass')
else:
    print('Fail')
'''
