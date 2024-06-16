lines=[]
print("Enter multiple lines of text(press enter when to end the line: )")
while True:
    line=input()
    if line=="":
        break
    lines.append(line)
print("\n You entered: ")
for line in lines:
    print(line)