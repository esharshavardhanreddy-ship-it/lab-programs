print("----- UNIT CONVERTER -----")

print("1. Kilometres to Miles")
print("2. Metres to Feet")
print("3. Celsius to Fahrenheit")
print("4. Kilograms to Pounds")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
    result = value * 0.621371
    print(value, "kilometres =", result, "miles")

elif choice == 2:
    result = value * 3.28084
    print(value, "metres =", result, "feet")

elif choice == 3:
    result = (value * 9 / 5) + 32
    print(value, "Celsius =", result, "Fahrenheit")

elif choice == 4:
    result = value * 2.20462
    print(value, "kilograms =", result, "pounds")

else:
    print("Invalid choice")