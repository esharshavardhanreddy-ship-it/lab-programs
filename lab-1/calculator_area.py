print("Simple Calculator")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")

print("\nArea Calculations")

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

print("Area of Rectangle:", length * breadth)

radius = float(input("Enter radius: "))
print("Area of Circle:", 3.14159 * radius * radius)