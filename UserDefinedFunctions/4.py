# Function that receives a list, modifies it, and returns a new list
def process_list(input_list):
    """
    Takes a list, performs operations, and returns a modified list
    Operations: 
    1. Squares all numbers
    2. Converts strings to uppercase
    3. Filters out non-number/string elements
    """
    result = []
    
    for item in input_list:
        if isinstance(item, (int, float)):
            result.append(item ** 2)  # Square numbers
        elif isinstance(item, str):
            result.append(item.upper())  # Uppercase strings
        # Other types are filtered out
    
    return result

# Function to demonstrate list modification without returning
def add_greeting_to_names(names_list):
    """Modifies the passed list by adding 'Hello ' before each name"""
    for i in range(len(names_list)):
        if isinstance(names_list[i], str):
            names_list[i] = "Hello " + names_list[i]
    # No return needed as we modified the original list

def main():
    # Example 1: Passing and returning a list
    original = [1, 2, 3, "apple", "banana", 4.5, True, None]
    print("Original list:", original)
    
    modified = process_list(original)
    print("Modified list (returned new list):", modified)
    print("Original list after function call (unchanged):", original)
    
    # Example 2: Modifying the passed list directly
    names = ["Alice", "Bob", "Charlie", 123]
    print("\nOriginal names list:", names)
    
    add_greeting_to_names(names)  # Modifies the list in-place
    print("Names list after modification:", names)
    
    # Example 3: Returning multiple lists
    def split_odd_even(numbers):
        """Returns two lists: odd numbers and even numbers"""
        odds = [x for x in numbers if isinstance(x, int) and x % 2 != 0]
        evens = [x for x in numbers if isinstance(x, int) and x % 2 == 0]
        return odds, evens
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_nums, even_nums = split_odd_even(numbers)
    print("\nOdd numbers:", odd_nums)
    print("Even numbers:", even_nums)

if __name__ == "__main__":
    main()