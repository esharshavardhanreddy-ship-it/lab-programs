
import json

# Sample log data
logs = [
    {"level": "INFO", "message": "Program started"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "INFO", "message": "User logged in"},
    {"level": "ERROR", "message": "Connection failed"},
    {"level": "INFO", "message": "Program completed"}
]

# Write logs into JSON file
with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

# Read JSON file
with open("logs.json", "r") as file:
    data = json.load(file)

# Count log levels
info = 0
warning = 0
error = 0

for log in data:
    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "WARNING":
        warning += 1
    elif log["level"] == "ERROR":
        error += 1

# Display analysis
print("--- LOG FILE ANALYSIS ---")
print("Total Logs:", len(data))
print("INFO Messages:", info)
print("WARNING Messages:", warning)
print("ERROR Messages:", error)

print("\n--- ERROR DETAILS ---")

for log in data:
    if log["level"] == "ERROR":
        print(log["message"])
