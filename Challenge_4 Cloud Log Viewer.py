""" 🎯 Goal:
Read from cloud_report.txt and display only the latest report entry (the most recent datetime + following lines until the next blank line). """

with open("cloud_report.txt", "r") as file:
    lines = file.readlines()

start_index = None
for i in range(len(lines) - 1, -1, -1):
    if "======" in lines[i]:
        start_index = i
        break

if start_index is not None:
    latest_report = lines[start_index:]
    print("".join(latest_report).strip())
else:
    print("No report found.")
