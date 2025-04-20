num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10          # Get the last digit
    reversed_num = reversed_num * 10 + digit
    num = num // 10           # Remove the last digit

print("Reversed number:", reversed_num)