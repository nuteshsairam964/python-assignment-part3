import requests
import copy
from datetime import datetime

# =========================
# TASK 1: FILE WRITE
# =========================

notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Write mode
with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")
print("File written successfully")

# Append mode
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions improve code reuse.\n")
    f.write("Topic 7: Modules help organize code.\n")
print("Lines appended")

# =========================
# TASK 1: FILE READ
# =========================

with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("\nNumbered Lines:")
for i, line in enumerate(lines, 1):
    print(f"{i}. {line.strip()}")

print("Total lines:", len(lines))

keyword = input("\nEnter keyword to search: ").lower()
found = False
for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found")

# =========================
# TASK 2: API
# =========================

def fetch_products():
    try:
        res = requests.get("https://dummyjson.com/products?limit=20", timeout=5)
        data = res.json()["products"]

        print("\nID | Title | Category | Price | Rating")
        print("-" * 60)

        for p in data:
            print(p["id"], "|", p["title"], "|", p["category"], "|", p["price"], "|", p["rating"])

        # Filter rating >= 4.5
        filtered = [p for p in data if p["rating"] >= 4.5]
        filtered.sort(key=lambda x: x["price"], reverse=True)

        print("\nFiltered (rating >= 4.5):")
        for p in filtered:
            print(p["title"], p["price"])

    except requests.exceptions.ConnectionError:
        log_error("fetch_products", "ConnectionError")
    except requests.exceptions.Timeout:
        log_error("fetch_products", "Timeout")
    except Exception as e:
        log_error("fetch_products", str(e))


def fetch_laptops():
    try:
        res = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
        data = res.json()["products"]

        print("\nLaptops:")
        for p in data:
            print(p["title"], p["price"])

    except Exception as e:
        log_error("fetch_laptops", str(e))


def post_product():
    try:
        data = {
            "title": "My Product",
            "price": 999,
            "category": "electronics"
        }
        res = requests.post("https://dummyjson.com/products/add", json=data)
        print("\nPOST Response:", res.json())

    except Exception as e:
        log_error("post_product", str(e))


# =========================
# TASK 3: EXCEPTION HANDLING
# =========================

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempted")


print("\nSafe Divide Tests:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

read_file_safe("python_notes.txt")
read_file_safe("ghost.txt")

# =========================
# TASK 4: LOGGING
# =========================

def log_error(func, message):
    with open("error_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] ERROR in {func}: {message}\n")


# Trigger errors intentionally
log_error("manual_test", "This is a test error")

# Run API
fetch_products()
fetch_laptops()
post_product()

# Print log file
print("\nError Log Content:")
with open("error_log.txt", "r") as f:
    print(f.read())
