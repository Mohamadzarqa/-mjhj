num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
x=input("enter the operation: ")
if x=="+":
    print(num1+num2)
elif x=="-":
    print(num1-num2)
elif x=="*":
    print(num1*num2)
else:
    if num2==0:
        print("error")
    else:
         print(num1/num2)
         
        
