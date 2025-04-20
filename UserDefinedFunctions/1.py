from datetime import datetime, timedelta

def calculate_days_late(return_date, due_date):
    """Calculate days between return date and due date"""
    delta = return_date - due_date
    return delta.days if delta.days > 0 else 0

def calculate_condition_fine(condition):
    """Calculate fine based on book condition"""
    condition = condition.lower()
    if condition == "excellent":
        return 0
    elif condition == "good":
        return 10
    elif condition == "fair":
        return 25
    elif condition == "poor":
        return 50
    elif condition == "damaged":
        return 100
    else:
        return 0  # default if condition not recognized

def calculate_total_fine(return_date_str, due_date_str, condition):
    """Calculate total fine combining late days and condition penalties"""
    try:
        # Convert string dates to datetime objects
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
        
        # Calculate days late
        days_late = calculate_days_late(return_date, due_date)
        
        # Calculate fines
        late_fine = days_late * 2  # ₹2 per day late
        condition_fine = calculate_condition_fine(condition)
        total_fine = late_fine + condition_fine
        
        # Generate report
        print("\n=== Library Fine Calculation ===")
        print(f"Due Date: {due_date}")
        print(f"Return Date: {return_date}")
        print(f"Days Late: {days_late}")
        print(f"Book Condition: {condition.capitalize()}")
        print("-----------------------------")
        print(f"Late Fine: ₹{late_fine}")
        print(f"Condition Fine: ₹{condition_fine}")
        print(f"Total Fine: ₹{total_fine}")
        
        return total_fine
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD")
        return 0

def main():
    print("Library Fine Calculator")
    print("Enter dates in YYYY-MM-DD format")
    
    # Get user input
    due_date = input("Enter due date (YYYY-MM-DD): ")
    return_date = input("Enter return date (YYYY-MM-DD): ")
    condition = input("Enter book condition (Excellent/Good/Fair/Poor/Damaged): ")
    
    # Calculate and display fine
    calculate_total_fine(return_date, due_date, condition)

if __name__ == "__main__":
    main()