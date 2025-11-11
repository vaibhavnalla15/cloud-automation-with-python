""" Goal:
Add automated alerting to your cloud monitoring script when resource usage exceeds limits. """

# Scenario:
# You manage multiple servers.
# If average CPU > 80% or average Memory > 75%, the system should print an alert message and log it in a separate file (alerts.txt).

from datetime import datetime

cpu_total = 0
mem_total = 0

# Input validation for number of servers
while True:
    try:
        servers = int(input("Enter number of servers: "))
        if servers <= 0:
            print("Number of servers must be greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter an integer.")

# Collect CPU and Memory data
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

# Calculate averages
avg_cpu = cpu_total / servers
avg_mem = mem_total / servers

# Display and log results
report = f"""
====== Cloud Resource Summary ======
Servers Monitored: {servers}
------------------------------
Total CPU Used: {cpu_total} vCPUs
Total Memory Used: {mem_total} GB
Average CPU per Server: {avg_cpu:.2f} vCPUs
Average Memory per Server: {avg_mem:.2f} GB
==============================
"""

print(report.strip())

# Alerts
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if avg_cpu > 80:
    print(f"⚠️ ALERT: High CPU Usage Detected (Average {avg_cpu:.2f}%)")
if avg_mem > 75:
    print(f"⚠️ ALERT: High Memory Usage Detected (Average {avg_mem:.2f}%)")
if avg_cpu <= 80 and avg_mem <= 75:
    print("✅ All resources healthy and within limits.")

# Save both report and alert to file
with open("alerts.txt", "a") as file:
    file.write(f"\n--- Report Generated at: {current_time} ---\n")
    file.write(report)
    if avg_cpu > 80 or avg_mem > 75:
        file.write(f"{current_time} - ALERT: CPU={avg_cpu:.2f}%, MEM={avg_mem:.2f}%\n")
    else:
        file.write("Status: All systems healthy\n")
