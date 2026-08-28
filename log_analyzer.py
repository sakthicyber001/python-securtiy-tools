from collections import Counter

filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    errors = [line for line in lines if "ERROR" in line.upper()]
    warnings = [line for line in lines if "WARNING" in line.upper()]

    print("\nLog Analysis")
    print("------------")
    print("Total lines:", len(lines))
    print("Errors:", len(errors))
    print("Warnings:", len(warnings))

except FileNotFoundError:
    print("Log file not found.")
