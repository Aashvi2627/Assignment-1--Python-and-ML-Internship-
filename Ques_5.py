a=str(input("Enter the text: "))
b=str(input("Enter filename with .txt extension: "))
with open(b,'w') as file:
    file.write(a)
print(f"Your text has been written to {b}")