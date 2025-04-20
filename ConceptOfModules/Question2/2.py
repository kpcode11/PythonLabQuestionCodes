def demonstrate_exceptions():
    while True:
        print("\nException Demonstration Menu:")
        print("1. Trigger NameError")
        print("2. Trigger IndexError")
        print("3. Trigger ZeroDivisionError")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        try:
            if choice == '1':
                # NameError demonstration
                print("\nAttempting to use an undefined variable...")
                print(undefined_variable)  # This variable doesn't exist
            
            elif choice == '2':
                # IndexError demonstration
                my_list = [10, 20, 30]
                print("\nCurrent list:", my_list)
                index = int(input("Enter an index to access (0-2): "))
                print("Value at index", index, "is:", my_list[index])
            
            elif choice == '3':
                # ZeroDivisionError demonstration
                numerator = int(input("\nEnter numerator: "))
                denominator = int(input("Enter denominator: "))
                result = numerator / denominator
                print("Division result:", result)
            
            elif choice == '4':
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice! Please enter 1-4")
        
        except NameError:
            print("Error: You tried to use a variable that doesn't exist!")
        
        except IndexError:
            print("Error: You tried to access an index that's out of range!")
            print("Remember list indices start from 0!")
        
        except ZeroDivisionError:
            print("Error: You cannot divide by zero!")
        
        except ValueError:
            print("Error: Please enter valid integers where required!")
        
        except Exception as e:
            print("An unexpected error occurred:", type(e).__name__, "-", e)
        
        else:
            print("Operation completed successfully!")
        
        finally:
            print("This always executes (cleanup can go here)")

# Run the demonstration
demonstrate_exceptions()