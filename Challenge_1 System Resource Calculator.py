""" 🎯 Goal
Simulate a small cloud resource monitoring script.
Your program calculates total and average CPU and memory usage across several servers.
This mimics a Cloud Engineer checking utilization across EC2 instances. """

# Input:
    # Number of servers (integer)
    # For each server:
        # CPU usage (float or int)
        # Memory usage (float or int)
# Output:
    # Total CPU usage (sum of all CPU inputs)
    # Total Memory usage (sum of all memory inputs)
    # Average CPU usage per server
    # Average Memory usage per server
# Constraints
    # Number of servers > 0
    # All input values must be positive numbers
    # Round average values to 2 decimal places

cpu_total = 0
mem_total = 0
servers = int(input("Enter number of servers: "))

for i in range(1, servers + 1):
    cpu = float(input(f"Enter CPU for server {i}: "))
    memory = float(input(f"Enter Memory for server {i}: "))
    if cpu <= 0 or memory <= 0:
        print("CPU and Memory must be positive values.")
        exit()
    cpu_total += cpu
    mem_total += memory

avg_cpu = cpu_total / servers
avg_mem = mem_total / servers

print(f"Total CPU used: {cpu_total} vCPUs")
print(f"Total Memory used: {mem_total} GB")
print(f"Average CPU per server: {avg_cpu:.2f} vCPUs")
print(f"Average Memory per server: {avg_mem:.2f} GB")


