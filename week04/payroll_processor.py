from employee import Employee

class PayrollProcessor:
    
    def __init__(self):
        self._employees = []
    
    @property
    def employees(self):
        return list(self._employees)
    
    def load_from_file(self, file):
        try:
            with open(file, "r") as file:
                for line in file:
                    line = line.strip()

                    if not line:
                        continue
                    parts = line.split("\t")

                    if len(parts) != 4:
                        print(f"Line: {line} skipped")
                        continue
                    try:
                        emp = Employee(parts[0], parts[1], float(parts[2]), float(parts[3]) )
                        self._employees.append(emp)
                    except ValueError as e:
                        print(f"Warning! Erron in '{line}': {e}")
        except FileNotFoundError:
            print("File was not found")
    
    def calculate_total_payroll(self):
        return sum(emp.calculate_gross_pay() for emp in self._employees)
    
    def find_highest_paid(self):
        if len(self._employees) == 0:
            return None
        
        highest = self._employees[0]
        
        for emp in self._employees:
            if emp.calculate_gross_pay() > highest.calculate_gross_pay():
                highest = emp
        
        return highest
    
    def find_lowest_paid(self):
        if len(self._employees) == 0:
            return None
        
        lowest = self._employees[0]

        for emp in self._employees:
            if emp.calculate_gross_pay() < lowest.calculate_gross_pay():
                lowest = emp
        
        return lowest
    
    def get_employee_count(self):
        return len(self._employees)
    
    def calculate_average_pay(self):
        count = self.get_employee_count()

        if count == 0:
            return 0.0
        
        total = self.calculate_total_payroll()
        return total / count
