a=int(input("Enter a no: "))
print(a)
factorial=1
if a<0:
    print("Factorial of a negative no is not defined")
elif a==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial *= i
        print(factorial)