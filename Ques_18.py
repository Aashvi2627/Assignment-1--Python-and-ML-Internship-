def are_anagrams(string1,string2):
    string1=string1.replace(" ","").lower()
    string2=string2.replace(" ","").lower()
    return sorted(string1)== sorted(string2)
string1=str(input("Enter string1: "))
string2=str(input("Enter string2: "))
if are_anagrams(string1,string2):
    print(f'"{string1}" and "{string2}" are anagrams')
else:
    print(f'"{string1}" and "{string2}" are not anagrams')