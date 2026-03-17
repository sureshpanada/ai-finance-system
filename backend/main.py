import datetime
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
    expenses = []

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
                print("Current expenses:", get_expenses(expenses))
        elif choice == '3':
                print("Exiting the application.")
                break
        else:   
                print("Invalid choice. Please try again.") 

def add_expense(expenses, name, amount):
    expense = {"name": name, "amount": amount, "date": str(date)}
    expenses.append(expense)
    print(f"Added expense: {expense}")    

def get_expenses(expenses):
    return expenses    

if __name__ == "__main__":
    start()   
   