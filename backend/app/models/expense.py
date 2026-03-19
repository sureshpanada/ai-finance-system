class Expense:
    def __init__(self, name, amount, date):
        if not name:
            raise ValueError("Expense name cannot be empty.")
        if amount <= 0:
            raise ValueError("Expense amount cannot be zero or negative.")

        self.name = name
        self.amount = amount
        self.date = date

    def __repr__(self):
        return (
            f"Expense(name={self.name!r}, amount={self.amount!r}, date={self.date!r})"
        )

    def __str__(self):
        return f"{self.name}: {self.amount} ({self.date})"

    def to_dict(self):
        return {"name": self.name, "amount": self.amount, "date": self.date}

    @staticmethod
    def from_dict(data):
        return Expense(
            name=data.get("name"), amount=data.get("amount"), date=data.get("date")
        )
