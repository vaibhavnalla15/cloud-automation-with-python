""" Goal:
Generate a summarized daily report of alerts collected in alerts.txt. """
# Requirements:-
# - Read alerts.txt.
# - Extract every timestamp after --- Report Generated at:.
# - Count how many alerts occurred for each date (e.g., 2025-11-06 → 4 alerts).
# - Compute daily average CPU and Memory values from the ALERT: lines.
# - Write a new file daily_summary.txt with content like:

from datetime import datetime

Date = "2025-11-11"
new_date = datetime.strptime(Date, "%Y-%m-%d").date()

# Step 1: Store alerts in a dictionary
alerts = {}
alert_logs = []

# Read and filter ALERT lines
with open("alerts.txt", "r") as file:
    for line in file:
        if "ALERT:" in line:
            alert_logs.append(line.strip())

# Parse each alert line
for log in alert_logs:
    # Example line: 2025-11-11 ALERT: CPU=80%, MEM=70%
    date_part, alert_part = log.split("ALERT: ")
    cpu, mem = alert_part.split(",")
    cpu_value = float(cpu.split("=")[1].replace("%", ""))
    mem_value = float(mem.split("=")[1].replace("%", ""))
    date_value = date_part.strip()

    # Store (cpu, mem) under each date
    if date_value not in alerts:
        alerts[date_value] = []
    alerts[date_value].append((cpu_value, mem_value))

# Step 2: Compute daily averages
report = {}
for date_value, values in alerts.items():
    total_cpu = sum(cpu for cpu, _ in values)
    total_mem = sum(mem for _, mem in values)
    count = len(values)
    avg_cpu = total_cpu / count
    avg_mem = total_mem / count
    report[date_value] = (avg_cpu, avg_mem)

# Step 3: Write summary report
with open("daily_summary.txt", "w") as f:
    for date_value, (avg_cpu, avg_mem) in report.items():
        f.write(f"{date_value}: Avg CPU={avg_cpu:.2f}%, Avg MEM={avg_mem:.2f}%\n")

print("Report generated successfully.")



