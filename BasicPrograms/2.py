# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Get range from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Swap if start is greater than end
if start > end:
    start, end = end, start

print(f"Prime numbers between {start} and {end} are:")

# Find and display prime numbers in the range
prime_numbers = []
for num in range(start, end + 1):
    if is_prime(num):
        prime_numbers.append(num)

if prime_numbers:
    print(*prime_numbers)
else:
    print("No prime numbers found in the given range.")