from pathlib import Path
import json
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent
DATA_FILE = PROJECT_ROOT / "expenseTrackerSAVING_system" / "data.json"

print("Data file location:", DATA_FILE)

# Load data
if DATA_FILE.exists():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        EXPENSE_COUNT = data.get("last_id", 0)
        CURRENTIE = data.get("currency", "")
    except:
        data = {}
        EXPENSE_COUNT = 0
        CURRENTIE = ""
else:
    data = {}
    EXPENSE_COUNT = 0
    CURRENTIE = ""

def START():
    global CURRENTIE, data
    if CURRENTIE:
        print(f"Last currency used: {CURRENTIE}")
        if input("Change currency? (y/n): ").strip().lower() != 'y':
            return

    CURRENTIE = input("Currency ($/£/€): ").strip()
    print(f"Currency set to: {CURRENTIE}")
    data["currency"] = CURRENTIE
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def ADD():
    global CURRENTIE, EXPENSE_COUNT, data

    if not CURRENTIE:
        START()

    try:
        amount = float(input(f"Amount {CURRENTIE} "))
    except ValueError:
        print("Invalid amount!")
        return

    description = input("Description: ").strip()


    date_input = input("Date (YYYY-MM-DD) [Enter = today]: ").strip()
    date = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

    print(f"\nAdded: {CURRENTIE}{amount:.2f} - {description} - {date}\n")

    EXPENSE_COUNT += 1
    key = f"expense{EXPENSE_COUNT}"

    data[key] = {
        "Amount": amount,
        "Description": description,
        "currency": CURRENTIE,
        "date": date
    }
    data["last_id"] = EXPENSE_COUNT

    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def CLEAR():
    global data, EXPENSE_COUNT
    if input("Delete ALL expenses? (y/n): ").strip().lower() != 'y':
        return

    saved_currency = data.get("currency", "")
    data = {"currency": saved_currency} if saved_currency else {}
    data["last_id"] = 0
    EXPENSE_COUNT = 0

    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Expenses cleared.")


def SHOW():
    if EXPENSE_COUNT == 0:
        print("No expenses recorded yet.")
        return

    print("\n" + "=" * 60)
    print("Your Expenses".center(60))
    print("=" * 60)

    total = 0
    for i in range(1, EXPENSE_COUNT + 1):
        key = f"expense{i}"
        if key in data:
            exp = data[key]
            # Use .get() with fallback value so it never crashes
            date_str = exp.get('date', '———')  # shows ——— when no date exists
            amount_str = f"{exp['currency']}{exp['Amount']:9.2f}"
            desc = exp['Description']

            print(f"{date_str} | {amount_str} | {desc}")
            total += exp['Amount']

    print("-" * 60)
    print(f"Total: {CURRENTIE}{total:9.2f}")
    print("=" * 60)


print("\n=== Expense Tracker ===\n")

if not CURRENTIE:
    START()

while True:
    print("\nCommands:  add    show    clear    change    quit")
    choice = input("→ ").strip().lower()

    if choice == "add":
        ADD()
    elif choice == "show":
        SHOW()
    elif choice == "clear":
        CLEAR()
    elif choice == "change":
        START()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command.")