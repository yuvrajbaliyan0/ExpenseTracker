class ExpensesTracker:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self,Expense):
        self.expenses.append(Expense)

    def delete_expense(self,Expense):
        self.expenses.remove(Expense)
    
    def sum_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
    def avg_expense(self):
        return int(sum(expense.amount for expense in self.expenses)/2)
    
    def filter_by_category(self,Category):
        filterlist = []
        for expense in self.expenses:
            if expense.category == Category:
                filterlist.append(expense)
        return filterlist
class Expense:
    def __init__(self,Name,Amount,Category):
        self.name = Name
        self.amount = Amount
        self.category = Category

    def __str__(self):
        return f"{self.name}, {self.amount},{self.category}"
    

tracker = ExpensesTracker()


expense1 = Expense("burger",0,"Resturant")
tracker.add_expense(expense1)

expense2 = Expense("pants",1400,"Wardrobe")
tracker.add_expense(expense2)

for expense in tracker.expenses:
    print(expense)

print(tracker.sum_expenses())

print(tracker.avg_expense())

for expense in tracker.filter_by_category("Wardrobe"):
    print(expense)
