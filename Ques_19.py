import string
def remove_punctuation(input_string):
    punctuation = string.punctuation
    result = ""
    for char in input_string:
        if char not in punctuation:
            result += char
    return result
input_string = str(input("Enter string: "))
clean_string = remove_punctuation(input_string)
print("Original String: ", input_string)
print("String without punctuation: ", clean_string)
