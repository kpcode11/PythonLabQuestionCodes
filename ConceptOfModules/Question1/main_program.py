from math_operations import factorial, primeNumber, powNumber

def main():
    while True:
        print("\nMENU")
        print("1. Calculate Factorial")
        print("2. Check Prime Number")
        print("3. Calculate Power")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            try:
                num = int(input("Enter a non-negative integer: "))
                print(f"Factorial of {num} is: {factorial(num)}")
            except ValueError:
                print("Please enter a valid integer!")
                
        elif choice == '2':
            try:
                num = int(input("Enter a number to check: "))
                if primeNumber(num):
                    print(f"{num} is a prime number")
                else:
                    print(f"{num} is not a prime number")
            except ValueError:
                print("Please enter a valid integer!")
                
        elif choice == '3':
            try:
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"{base}^{exponent} = {powNumber(base, exponent)}")
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == '4':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please enter 1-4")

if __name__ == "__main__":
    main()