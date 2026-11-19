
import csv

# Create and write employee details
with open("payroll.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Basic Salary", "Allowance", "Deduction"])

    writer.writerow(["harsha", 20000, 3000, 1000])
    writer.writerow(["kayadu", 25000, 4000, 1500])
    writer.writerow(["shraddha", 30000, 5000, 2000])

# Read and calculate payroll
with open("payroll.csv", "r") as file:
    reader = csv.DictReader(file)

    print("--- PAYROLL REPORT ---")

    for row in reader:
        name = row["Name"]
        basic = float(row["Basic Salary"])
        allowance = float(row["Allowance"])
        deduction = float(row["Deduction"])

        net_salary = basic + allowance - deduction

        print("\nEmployee:", name)
        print("Basic Salary:", basic)
        print("Allowance:", allowance)
        print("Deduction:", deduction)
        print("Net Salary:", net_salary)
