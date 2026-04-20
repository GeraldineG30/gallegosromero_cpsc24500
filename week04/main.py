from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport

def main():
    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")

    report = PayrollReport(processor)

    while True:
        print("\n" + "=" * 65 )
        print("%45s" % ("PAYROLL MANAGEMENT SYSTEM"))
        print("=" * 65 + "\n")
        print("1. View all employees")
        print("2. View payroll summary")
        print("3. Generate report file")
        print("4. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            report.display_all_employees()
        elif choice == "2":
            report.display_payroll_summary()
        elif choice == "3":
            file = input("\nEnter file name: ")
            report.generate_report_file(file)
            print("\nReport successfully generated")
        elif choice == "4":
            print("\nGoodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
