import datetime
import json

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

        if choice == '1':
                name = input("Enter expense name: ")
                amount = float(input("Enter expense amount: "))
                add_expense(expenses, name, amount)
        elif choice == '2':
                print("Current expenses:", get_expenses())
        elif choice == '3':
                print("Exiting the application.")
                break
        else:   
                print("Invalid choice. Please try again.") 

def add_expense(expenses, name, amount):
    expense = {"name": name, "amount": amount, "date": str(date)}
    expenses.append(expense)
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)
    # print(f"Added expense: {expense}")    

def get_expenses():
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    start()   
   