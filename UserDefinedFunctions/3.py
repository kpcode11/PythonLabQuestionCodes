def fibonacci(n):
    """Recursive function to return the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def display_fibonacci_series(n):
    """Display Fibonacci series up to n elements"""
    print(f"Fibonacci series (first {n} elements):")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()  # For new line

# Main program
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of Fibonacci elements to display: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            display_fibonacci_series(n)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")