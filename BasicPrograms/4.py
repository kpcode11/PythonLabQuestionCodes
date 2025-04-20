def number_pattern(rows):
    print("\nNumber Pattern (Right-angled Triangle):")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def star_pattern(rows):
    print("\nStar Pattern (Pyramid):")
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()

# Main program
print("Pattern Selector")
print("1. Number Pattern (Right-angled Triangle)")
print("2. Star Pattern (Pyramid)")

choice = int(input("Enter your choice (1 or 2): "))
rows = int(input("Enter the number of rows: "))

if choice == 1:
    number_pattern(rows)
elif choice == 2:
    star_pattern(rows)
else:
    print("Invalid choice! Please enter either 1 or 2.")