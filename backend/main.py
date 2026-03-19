import datetime
import json
from app.models.expense import Expense

date = datetime.datetime.now()


def start():
    print("Starting the backend server...")

    # Here you would typically set up your server, routes, database connections, etc.
    # For example, if you're using Flask:
    # from flask import Flask
    # app = Flask(__name__)
    # @app.route('/')
    # def home():
    #     return "Hello, World!"
    # app.run(debug=True)
    expenses = get_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                name = input("Enter expense name: ").strip()
                amount = float(input("Enter expense amount: "))
                add_expense(expenses, name, amount)
            except ValueError as e:
                print(f"Error: {e}")
                continue
        elif choice == "2":
            if not expenses:
                print("No expenses found.")
            else:
                print("Current expenses:", get_expenses())
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


def add_expense(expenses, name, amount):
    expense = Expense(name, amount, str(date))
    expenses.append(expense.to_dict())
    try:
        with open("expenses.json", "w") as f:
            json.dump(expenses, f, indent=4)
    except Exception as e:
        print(f"Error saving expense: {e}")
    # print(f"Added expense: {expense}")


def get_expenses():
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
        print(f"Total entries: {len(expenses)}")
        return [Expense.from_dict(expense) for expense in expenses]
        # return expenses
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from expenses.json. Returning empty list.")
        return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []


if __name__ == "__main__":
    start()
