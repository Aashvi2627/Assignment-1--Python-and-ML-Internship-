input_string = str(input("Enter string: "))
frequency = {}
for char in input_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for char, count in frequency.items():
    print(f"'{char}': {count}")