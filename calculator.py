#in this calculator you can only add,sub,multiply or divide with onlr two num only
print("enter the operator")
#operators are +,-,*,/
operator=input()
print("enter the first number")
num1=int(input())
print("enter the second number")
num2=int(input())
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)    
else:
    print("invalid operator")