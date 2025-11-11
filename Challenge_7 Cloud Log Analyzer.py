""" Goal:
Write a Python script that scans your alerts.txt file and counts how many High CPU and High Memory alerts occurred.
At the end, display the total count for each type. """
from pprint import pprint

# Constraints
# - A “High CPU” alert means CPU > 80%.
# - A “High Memory” alert means Memory > 75%.
# - File may contain healthy lines (ignore them).
# - Use simple parsing (no regex required yet).

high_cpu = 0
high_mem = 0
total_alerts = 0
alert_logs = []
try:
    with open("alerts.txt", "r") as file:
        for line in file:
            if "ALERT:" in line:
                alert_logs.append(line)

    for log in alert_logs:
        parts = log.split("ALERT: ")[1]
        cpu, mem = parts.split(",")
        cpu_value = float(cpu.split("=")[1].replace("%", ""))
        mem_value = float(mem.split("=")[1].replace("%", ""))

        if cpu_value > 80:
            high_cpu += 1
        if mem_value > 75:
            high_mem += 1

    total_alerts = len(alert_logs)

    print(f"Total High CPU Alerts: {high_cpu}")
    print(f"Total High Memory Alerts: {high_mem}")
    print(f"Total Combined Alerts: {total_alerts}")

except FileNotFoundError:
    print("Please Enter correct file name")






