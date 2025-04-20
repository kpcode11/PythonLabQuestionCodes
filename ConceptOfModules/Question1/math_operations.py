def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Factorial doesn't exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

def primeNumber(num):
    """Check if a number is prime"""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

def powNumber(base, exponent):
    """Calculate power of a number"""
    return base ** exponent