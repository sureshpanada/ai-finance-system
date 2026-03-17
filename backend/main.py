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

    add_expense(expenses, "Groceries", 150)
    add_expense(expenses, "Rent", 1200)
    add_expense(expenses, "Utilities", 200)

    print("Current expenses:", get_expenses(expenses))
    print("typeof expenses:", type(expenses))
    print("typeof get_expenses:", type(get_expenses(expenses)))
    print("type of each expense:", type(expenses[0]))

    for expense in expenses:
        print(f"Expense: {expense}, Type: {type(expense)}")  

def add_expense(expenses, name, amount):
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    print(f"Added expense: {expense}")    

def get_expenses(expenses):
    return expenses    

if __name__ == "__main__":
    start()   
   