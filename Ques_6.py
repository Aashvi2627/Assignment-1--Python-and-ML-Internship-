filename=str(input("Enter text as .txt extension: "))
try:
    with open(filename,'r') as file:
        content=file.read()
        print("File content: ")
        print(content)
except FileNotFoundError:
    print("File does not exist")
except IOError:
    print(f"Error occured while reading the file")