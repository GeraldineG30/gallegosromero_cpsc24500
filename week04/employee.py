class Employee:
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # Setters 
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = float(hours_worked)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def employee_id(self):
        return self._employee_id
    
    @employee_id.setter
    def employee_id(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Employee Id cannot be empty")
        self._employee_id = value
    
    @property
    def hourly_rate(self):
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Hourly rate cannot be empty")
        self._hourly_rate = value
    
    @property
    def hours_worked(self):
        return self._hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value):
        value = float(value)
        if value < 0 or value > 168:
            raise ValueError("Hours can not be negative or greater than 168")
        self._hourly_worked = value

    def calculate_gross_pay(self):
        regular_pay = min(self.hours_worked, 40) * self.hourly_rate
        overtime_pay = max(self.hours_worked - 40, 0) * self.hourly_rate * 1.5

        return regular_pay + overtime_pay
    
    def __str__(self):
        return f"{self.name} {self.employee_id} ${self.hourly_rate} {self.hours_worked} ${self.calculate_gross_pay():2f}"
    