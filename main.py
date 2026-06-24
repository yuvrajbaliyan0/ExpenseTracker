class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,Expense):
        self.expenses.append(Expense)

    def delete_expense(self,Expense):
        self.expenses.remove(Expense)

    def sum_expense(self):
        return sum(expense.amount for expense in self.expenses)
    
    def filtered_by_category(self,Category):
        filteredlist = []
        for expense in self.expenses:
            if expense.category == Category:
                filteredlist.append(expense)
        return filteredlist

class Expense:
    def __init__(self,Name,Amount,Category):
        self.name = Name
        self.amount = Amount 
        self.category = Category
    
    def __str__(self):
        return f"{self.name},{self.amount},{self.category}"

#Manager of tracker
tracker = ExpenseTracker()    

#ADD EXPENSES.............................................................................................................

#Expense1
expense1 = Expense("Burger",100,"Resturant")
tracker.add_expense(expense1)

#Expense2
expense2 = Expense("jogger and shoes", 5000,"Wardrobe")
tracker.add_expense(expense2)

#Expense3 
expense3 = Expense("netflix",500,"Entertainment")
tracker.add_expense(expense3)

#Expense4 
expense4 = Expense("spotify",100,"Entertainment")
tracker.add_expense(expense4)

#Expense5 
expense5 = Expense("benQ Monitor and samsung phone",50000,"Tech and Gadget")
tracker.add_expense(expense5)

#DELETE EXPENSES...............................................................................................................




#GIVE LIST OF EXPENSES.........................................................................................................
for expense in tracker.expenses:
    print(expense)



#SUM OF TOTAL EXPENSES.........................................................................................................
print(tracker.sum_expense())

for expense in tracker.filtered_by_category("Entertainment"):
    print(expense)