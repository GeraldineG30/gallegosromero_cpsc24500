class PayrollReport:
    def __init__(self, processor):
        self._processor = processor

    def display_all_employees(self):
        print("=" * 65)
        print("%-15s %-10s %10s %10s %12s" % ("Name", "ID", "Rate", "Hours", "Gross Pay"))
        print("=" * 65)

        for emp in self._processor.employees:
            print(emp)
    
    def display_payroll_summary(self):
        print("\n--- Payroll Summary ---")

        print(f"Total employees: {self._processor.get_employee_count()}")
        print(f"Total payroll: ${self._processor.calculate_total_payroll():.2f}")
        print(f"Average pay: ${self._processor.calculate_average_pay():.2f}")

        highest = self._processor.find_highest_paid()
        lowest = self._processor.find_lowest_paid()

        if highest:
            print(f"Highest paid: {highest.name} (${highest.calculate_gross_pay():.2f})")
        if lowest:
            print(f"Lowest paid: {lowest.name} (${lowest.calculate_gross_pay():.2f})")
    
    def generate_report_file(self, file):
        with open(file, "w") as f:
            
            f.write("=" * 65 + "\n")
            f.write("%-15s %-10s %10s %10s %12s" % ("Name", "ID", "Rate", "Hours", "Gross Pay\n"))
            f.write("=" * 65 + "\n")

            for emp in self._processor.employees:
                f.write(str(emp) + "\n")
            
            f.write("=" * 65 + "\n")
            f.write("Payroll summary\n")
            f.write("=" * 65 + "\n")

            f.write(f"Total employees: {self._processor.get_employee_count()}\n")
            f.write(f"Total payroll: ${self._processor.calculate_total_payroll():.2f}\n")
            f.write(f"Average pay: ${self._processor.calculate_average_pay():.2f}\n")

            highest = self._processor.find_highest_paid()
            lowest = self._processor.find_lowest_paid()

            if highest:
                f.write(f"Highest paid: {highest.name} (${highest.calculate_gross_pay():.2f})\n")
            if lowest:
                f.write(f"Lowest paid: {lowest.name} (${lowest.calculate_gross_pay():.2f})\n")