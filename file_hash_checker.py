import hashlib

filename = input("Enter file name: ")

try:
    with open(filename, "rb") as file:
        file_hash = hashlib.sha256(file.read()).hexdigest()

    print("\nSHA-256 File Hash:")
    print(file_hash)

except FileNotFoundError:
    print("File not found.")
