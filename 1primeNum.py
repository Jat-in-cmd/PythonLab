n=int(input("enter the number :"))
flag=0
for x in range(2,n):
    if(n%x==0):
        flag=1
            
if(flag==1): print("it is not a prime number ")
if(flag!=1): print("it is a prime number ")