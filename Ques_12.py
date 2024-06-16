number=int(input("Enter number: "))
number = abs(number)
digits = str(number)
total_sum = 0
for digit in digits:
    total_sum += int(digit)
print(f"The sum of the digits of {number} is {total_sum}")