import hashlib

text = input("Enter text to hash: ")

sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("\nSHA-256 Hash:")
print(sha256_hash)
