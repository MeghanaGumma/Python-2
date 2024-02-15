sno=int(input("Enter Sno: "))
sname=input("Enter Sname: ")
gr=input("Enter Group: ")
s1=float(input("Enter S1 marks: "))
s2=float(input("Enter S2 marks: "))
s3=float(input("Enter S3 marks: "))
t=s1+s2+s3
avg=t/3
print("\nSNO = ",sno,"\nSNAME = ",sname,"\nGROUP = ",gr,"\nTOTAL MARKS = ",t,"\nAVERAGE = ",avg)
if avg>=90:
    print("O GRADE")
elif avg>=80:
    print("A GRADE")
elif avg>=70:
    print("B GRADE")
elif avg>=60:
    print("C GRADE")
elif avg>=50:
    print("D GRADE")
else:
    print("FAIL")
