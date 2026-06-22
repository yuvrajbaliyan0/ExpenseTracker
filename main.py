#Create a class where all app function like sum add delete category are exist.
class ExpenseTracker:

    #when call class or create object first its seperate Expenses list create.
    def __init__(self):
        self.expenses = []
    
    #add item in Expenses List...............
    def add_expense(self,expense):
        self.expenses.append(expense)

    #delete item in Expenses List.............
    def delete_expense(self,expense):
        self.expenses.remove(expense)

    #Sum items in Expenses List................
    def sum_expense(self):
        return sum(expense.Amount for expense in self.expenses)
    
    #Filter items from Expenses List by category Name....................
    def filter_by_category(self,category):
        filtered = []
        for expense in self.expenses:
            if expense.Category == category:
                filtered.append(f"{expense.Name} = {expense.Amount}")
        return filtered
               

#create an expense class with name,amount, category
class Expense:
    #when make a object, stores parameter of it in variable by call Expense class
    def __init__(self,name,amount,category):
        self.Name= name
        self.Amount= amount
        self.Category = category
    
    
    #display or convert object as text rather than something like"[<__main__.Expense object at 0x000001>, <__main__.Expense object at 0x000002>]"
    def __str__(self):
        return f"{self.Name} ,{self.Amount}, {self.Category}"
    
    


#CALLING CLASS AND ITS FUNCTION ------------------------//--------------------------//----------------------------------//--------------------------------------------

#Manager of expense
tracker = ExpenseTracker()

#ADD AN EXPENSE  ------------------------------------------------------------------------------------------------------------------------------------------------------

#Burger (Expense1) 
burger= Expense("Burger",100,"resturant")#expense 1
tracker.add_expense(burger)#store or add expense in list by add function through Tracker variable which call ExpenseTracker class.

#Shoes (Expense2) 
shoes = Expense("shoes",1500,"wardrobe")#expense 2
tracker.add_expense(shoes)#store or add expense in list by add function through Tracker variable which call ExpenseTracker class.

#DELETE AN EXPENSE -----------------------------------------------------------------------------------------------------------------------------------------------------



#PRINT EXPENSES IN Expenses List ----------------------------------------------------------------------------------------------------------------------------------------
for expense in tracker.expenses:
    print(expense)

#SUM AN EXPENSES----------------------------------------------------------------------------------------------------------------------------------------------------------
print(tracker.sum_expense())

#FILTER EXPENSES FROM LIST BY THEIR CATEGORY------------------------------------------------------------------------------------------------------------------------------
for filterexpense in tracker.filter_by_category("wardrobe"):
    print(filterexpense)