destination_file = input("Enter the path of the destination file: ")
try:
    with open(source_file, 'r') as src:
        contents = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(contents)
except FileNotFoundError:
    print(f"Error: {source_file} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")