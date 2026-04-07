# Super class
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary # monthly salary (for full-time)

    def calaculate_annual_salary(self):
        # Calculates salary for a generic employee.
        # Default assumption: Salary is monthly.
        return self.salary * 12
    
# Subclass 1: Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        # Call the parent constructor
        super().__init__(name, salary)
        self.bonus = bonus

    def calaculate_annual_salary(self):
        # Overrides parent method
        # Annual Salary = (monthly salary * 12) + bonus
        return (self.salary * 12) + self.bonus
    
# Subclass 2: Part-Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, name: str, hours_worked: float, hourly_rate: float):
        # Call the parent constructor with salary = 0 ( not used directly)
        super().__init__(name, 0)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calaculate_annual_salary(self):
        # Overrides parent method. 
        # Annual salary = hours worked * hourly rate(Assuming total hours already represent a yearly total)
        return self.hours_worked * self.hourly_rate
    


# TEST SCRIPT
if __name__ == "__main__":
    # Create full-time employee
    full_time = FullTimeEmployee("Emmanuel", 3000, 5000)

    # Create part-time employee
    part_time = PartTimeEmployee("Ama", 1200, 15)

    print("=== Full-Time Employee ===")
    print("Name: ", full_time.name)
    print("Annual Salary: ", full_time.calaculate_annual_salary())

    print("\n=== Part-Time Employee ===")
    print("Name: ", part_time.name)
    print("Annual Salary: ", part_time.calaculate_annual_salary())