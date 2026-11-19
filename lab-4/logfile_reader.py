
# Log File Reader Program

# Create a log file
with open("log.txt", "w") as file:
    file.write("INFO: Program started\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: Program completed\n")

# Read the log file
with open("log.txt", "r") as file:
    print("--- LOG FILE CONTENTS ---")
    for line in file:
        print(line.strip())
