class Employee:
    # Class variable
    company = "ABC Corp"
    
    # Default Constructor (no parameters)
    def __init__(self):
        self.name = "New Employee"
        self.id = 0000
        self.salary = 0.0
        print("Default constructor called - Employee created with default values")
    
    # Parameterized Constructor
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary
        print(f"Parameterized constructor called - Employee {self.name} created")
    
    def display_info(self):
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {Employee.company}")

class Laptop:
    # Default Constructor
    def __init__(self):
        self.brand = "Dell"
        self.model = "XPS 15"
        self.price = 1499.99
        print("\nDefault constructor called - Laptop created with default values")
    
    def display_specs(self):
        print(f"\nLaptop Specifications:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")

# Main program
if __name__ == "__main__":
    print("=== Constructor Demonstration ===")
    
    # Creating objects using different constructors
    print("\nCreating Employee objects:")
    emp1 = Employee("John Doe", 1001, 75000.50)  # Parameterized constructor
    emp1.display_info()
    
    print("\nCreating Laptop objects:")
    laptop1 = Laptop()  # Default constructor
    laptop1.display_specs()
    
    # Creating another employee
    emp2 = Employee("Jane Smith", 1002, 82000.75)
    emp2.display_info()