""" 🎯 Goal
Upgrade your previous “System Resource Calculator” to make it more realistic and fault-tolerant, like a script a Cloud Engineer might run to verify resource reports before sending data to monitoring systems. """

# Your program should:
# Validate that all CPU and Memory inputs are positive numbers.
# Handle wrong inputs (like text or negative values) gracefully using try/except.
# At the end, display a well-formatted summary report.

# 📥 Input
# Number of servers (integer)
# For each server:
# CPU usage (float, must be > 0)
# Memory usage (float, must be > 0)
# If user enters invalid data (e.g., negative or text), prompt again.

cpu_total = 0
mem_total = 0

while True:
    try:
        servers = int(input("Enter number of servers: "))
        if servers <= 0:
            print("Number of servers must be greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter an integer.")

for i in range(1, servers + 1):
    while True:
        try:
            cpu = float(input(f"Enter CPU for server {i}: "))
            memory = float(input(f"Enter Memory for server {i}: "))
            if cpu <= 0 or memory <=0:
                print("CPU and Memory must be positive values.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    cpu_total += cpu
    mem_total += memory

avg_cpu = cpu_total / servers
avg_mem = mem_total / servers

print("\n====== Cloud Resource Summary ======")
print(f"Servers Monitored: {servers}")
print("------------------------------")
print(f"Total CPU Used: {cpu_total} vCPUs")
print(f"Total Memory Used: {mem_total} GB")
print(f"Average CPU per Server: {avg_cpu:.2f} vCPUs")
print(f"Average Memory per Server: {avg_mem:.2f} GB")
print("==============================")