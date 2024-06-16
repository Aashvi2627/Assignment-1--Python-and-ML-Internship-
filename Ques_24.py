a=float(input("Enter number 1: "))
b=float(input("Enter number 2: "))
operator=input("Enter operator from (+) , (-) , (/) , (*): ")
if operator == '+':
    sum=a+b
    print("Sum is: ", sum)
elif operator == '-':
    if (a>b):
        sub=a-b
        print("Subtraction is:", sub)
    else:
        sub=b-a
        print("Subtraction is: ", sub)
elif operator == '/':
    division=a/b
    print("Division is: ", division)
else:
    multiply=a*b
    print("Multiplication is: ", multiply)