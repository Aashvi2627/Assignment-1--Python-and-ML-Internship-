string=str(input("Enter string: "))
suffix=input("Enter suffix: ")
prefix=input("Enter prefix: ")
if string[0]==prefix:
    print("Yes string starts with the given prefix")
else:
    print("No, the given string does not start with the given prefix")
if string[-1]==suffix:
    print("Yes the string ends with the given suffix")
else:
    print("No, the string does not end with the given suffix")