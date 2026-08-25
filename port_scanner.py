import socket

target = input("Enter IP address or hostname: ")

print(f"\nScanning {target}...")

for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")

    sock.close()
