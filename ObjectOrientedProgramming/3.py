# Single-Level Inheritance Example
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"{self.__class__.__name__} instance created")

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):  # Single inheritance
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)  # Using super() to call parent's __init__
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()} with {self.num_doors} doors"

    def honk(self):
        print("Beep beep!")

# Multilevel Inheritance Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.__class__.__name__} instance created")

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"

class Employee(Person):  # First level inheritance
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.department = None

    def __str__(self):
        return f"{super().__str__()} | ID: {self.emp_id}"

    def assign_department(self, dept):
        self.department = dept
        print(f"{self.name} assigned to {dept} department")

class Manager(Employee):  # Second level inheritance (multilevel)
    def __init__(self, name, age, emp_id, team_size):
        super().__init__(name, age, emp_id)
        self.team_size = team_size

    def __str__(self):
        return f"{super().__str__()} | Manager of {self.team_size} people"

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting with {self.team_size} team members")

def main():
    print("\n=== Single-Level Inheritance Demo ===")
    my_car = Car("Toyota", "Camry", 2022, 4)
    print(my_car)  # Uses Car's __str__
    my_car.start_engine()  # Inherited from Vehicle
    my_car.honk()  # Car's own method

    print("\n=== Multilevel Inheritance Demo ===")
    manager = Manager("Sarah Johnson", 35, "MGR100", 8)
    print(manager)  # Uses Manager's __str__
    manager.assign_department("Marketing")  # Inherited from Employee
    manager.conduct_meeting()  # Manager's own method

if __name__ == "__main__":
    print(f"\nRunning {__name__} program")
    main()