
a=int(input("Enter your age is: "))
print("Your age is : ",a)
b=int(input("Enter your number: "))
# conditional operators   >,<,<=,!,!=,==
if(a>18):
   print("You can drive")
elif(a==18):
    print("license nikalva toh")
else:
   print("You cannot drive")

if(b<0):
    print("b is negative")
elif(b>0):
    if(b<=10):
       print("b is between 0-10")
    elif(b<=20):
       print("b is between 0-20")
    else:
        print("b is not between 0-20")
else:
    print("b is zero")
