def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
choice=input("Which operator do you want to use? [+,-,*,/]=")
num1=int(input("Enter the first number="))
num2=int(input("Enter the second number="))
if choice=='+':
    print(num1," + ",num2," = ",addition(num1,num2))
elif choice=='-':
    print(num1," - ",num2," = ",subtraction(num1,num2))
elif choice=='*':
    print(num1," * ",num2," = ",multiply(num1,num2))
elif choice=='/':
    print(num1," / "+num2," = ",divide(num1,num2))