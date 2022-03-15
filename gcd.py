a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
r=1
if a<b :
    a,b=b,a
   
if a==0:
    print("GCD (",a,",",b,") is",b)
elif b==0:
    print("GCD (",a,",",b,") is",a)

else:
    while(r!=0):
        r=a%b
        a=b
        b=r
        print("GCD (",a,",",b,") is",a)
