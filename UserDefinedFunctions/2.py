class Employee:
    def __init__(self, emp_id, name, emp_type):
        self.emp_id = emp_id
        self.name = name
        self.emp_type = emp_type
        self.tax_rate = 0.10  # 10% income tax
    
    def calculate_net_salary(self):
        pass  # To be implemented in child classes
    
    def display_salary_slip(self, basic, deductions, allowances, net):
        print("\n=== Salary Slip ===")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.emp_type}")
        print("-----------------------------")
        print(f"Basic Salary: ₹{basic:.2f}")
        print(f"Allowances: ₹{allowances:.2f}")
        print(f"Deductions: ₹{deductions:.2f}")
        print("-----------------------------")
        print(f"Net Salary: ₹{net:.2f}")
        print("=============================")

class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, "Permanent")
        self.monthly_salary = monthly_salary
        self.pf_rate = 0.12  # 12% PF
    
    def calculate_net_salary(self, present_days, bonus=0):
        total_days = 22  # Working days in month
        basic = (self.monthly_salary / total_days) * present_days
        
        # Deductions
        pf = basic * self.pf_rate
        tax = basic * self.tax_rate
        deductions = pf + tax
        
        # Allowances
        allowances = bonus
        
        net_salary = basic + allowances - deductions
        self.display_salary_slip(basic, deductions, allowances, net_salary)
        return net_salary

class TemporaryEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate):
        super().__init__(emp_id, name, "Temporary")
        self.hourly_rate = hourly_rate
    
    def calculate_net_salary(self, hours_worked, overtime=0, bonus=0):
        regular_hours = min(hours_worked, 176)  # 176 = 22 days * 8 hours
        overtime_hours = max(hours_worked - 176, 0)
        
        # Basic pay calculations
        basic = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
        
        # Deductions
        tax = (basic + overtime_pay) * self.tax_rate
        deductions = tax
        
        # Allowances
        allowances = overtime_pay + overtime + bonus
        
        net_salary = basic + allowances - deductions
        self.display_salary_slip(basic, deductions, allowances, net_salary)
        return net_salary

def main():
    print("Employee Salary Calculator")
    
    # Permanent Employee Calculation
    print("\nPermanent Employee Details:")
    perm_emp = PermanentEmployee("P1001", "Rahul Sharma", 50000)
    present_days = int(input("Enter present days (out of 22): "))
    bonus = float(input("Enter bonus amount (₹): "))
    perm_emp.calculate_net_salary(present_days, bonus)
    
    # Temporary Employee Calculation
    print("\nTemporary Employee Details:")
    temp_emp = TemporaryEmployee("T2001", "Priya Patel", 250)
    hours_worked = float(input("Enter total hours worked: "))
    overtime = float(input("Enter overtime bonus (₹): "))
    bonus = float(input("Enter performance bonus (₹): "))
    temp_emp.calculate_net_salary(hours_worked, overtime, bonus)

if __name__ == "__main__":
    main()