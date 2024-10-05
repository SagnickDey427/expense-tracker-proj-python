class Expense:
    def __init__(self,name,catagory,amount):
        Expense.name=name
        Expense.amount=amount
        Expense.catagory=catagory
    def __repr__(self):
        return f"[expense name:'{Expense.name}' catagory:'{Expense.catagory}' amount:₹{Expense.amount}]"
