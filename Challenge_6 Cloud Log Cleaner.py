""" Goal:
Create a Python script that automatically checks the size of your log file (alerts.txt).
If it exceeds 1 MB, the program should archive it with a timestamped name and create a new empty log file. """


# ==> Input:
# - File name: "alerts.txt" (already exists).

# ==> Output:
# - If file size > 1 MB → rename it as alerts_YYYYMMDD_HHMMSS.txt, and create a fresh "alerts.txt".
# - Else → print "Log file size normal. No rotation needed."

# ==> Constraints
# - Assume file exists in the same directory.
# - File size limit = 1 MB (1_000_000 bytes).
# - Use os.path.getsize() and os.rename() for file operations.

from datetime import datetime
import os

file_name = "alerts.txt"

if not os.path.exists(file_name):
    print("No log file found.")
else:
    file_size = os.path.getsize(file_name)
    date = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_size > 1_000_000:
        new_name = f"alerts_{date}.txt"
        os.rename(file_name, new_name)
        open(file_name, "w").close()
        print(f"Log rotated. Old file renamed to {new_name}")
    else:
        print("Log file size normal. No rotation needed.")

