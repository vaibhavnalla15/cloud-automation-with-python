""" 🎯 Goal
Extend your previous script so it automatically writes the summary report to a file, simulating how a Cloud Engineer logs system data or automation results for auditing. """

# You’ll still collect CPU and memory usage, but now also:
# - Save results in a .txt file.
# - Append new runs to the same file, not overwrite it.

# 📥 Input
# - Number of servers.
# - CPU and Memory usage for each server (validated like before).


from datetime import datetime
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
            if cpu <= 0 or memory <= 0:
                print("CPU and Memory must be positive values.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    cpu_total += cpu
    mem_total += memory

avg_cpu = cpu_total / servers
avg_mem = mem_total / servers

report = f"""
====== Cloud Resource Summary ======
Servers Monitored: {servers}
------------------------------
Total CPU Used: {cpu_total} vCPUs
Total Memory Used: {mem_total} GB
Average CPU per Server: {avg_cpu:.2f} vCPUs
Average Memory per Server: {avg_mem:.2f} GB
==============================\n
"""

with open("cloud_report.txt", "a") as file:
    current_datetime = datetime.now()
    file.write(f"{current_datetime}\n")
    file.write(report)


