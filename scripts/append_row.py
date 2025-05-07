import sqlite3
import csv
import os

# File paths (used by both local and docker setups)
#test git
DB_PATH = "data/example.db"

CSV_PATH = "output/users.csv"

def append_latest_user():
    # Connect to SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch the latest user (by id)
    cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()

    if not row:
        print("No users found.")
        return

    # Get column names
    column_names = [desc[0] for desc in cursor.description]

    # Make sure the output folder exists
    os.makedirs("output", exist_ok=True)

    # Write (append) to CSV
    write_header = not os.path.exists(CSV_PATH)
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(column_names)
        writer.writerow(row)

    print(f"✅ Appended row to {CSV_PATH}")
    conn.close()

# Uncomment to run manually for testing
if __name__ == "__main__":
  append_latest_user()