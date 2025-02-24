class BudgetTracker:
    def __init__(self):
        self.income = 500
        self.expenses = {}
        
    def add_income(self, amount):
        self.income += amount
        print(f"Added income: ${amount: .2f}")
        
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else: self.expenses[category] = amount
        print(f"added expense: ${amount: .2f} for {category}")
        
    def get_total_expenses(self):
        return sum(self.expenses.values())
    
    def get_balance(self):
        return self.income - self.get_total_expenses()

        
    def show_expense_breakdown(self):
        print("\nExpense Breakdown:")
        for category, amount in self.expenses.items():
            print(f" {category}: ${amount: .2f}")
            
    def show_summary(self):
        total_expenses = self.get_total_expenses()
        balance = self.get_balance()
        
        print("\nBudget summary")
        print(f" Total Income: ${self.income:.2f}")
        Print(f "Total Expenses: ${total_expenses:.2f}")
        Print(f "Remaining Balance: ${balance:.2f}")

    def main():
        budget = BudgetTracker()
        
        while True:
            Print("\nBudget Tracker Menu")
            Print("1. Add Income")
            Print("2. Add Expense")
            Print("3. Show Budget Summary")
            Print("4. Show Expenses Breakdown")
            Print("5. Exit")
            
            choice = input("choose an option: ")
            
            if choice == "1"
                amount = float(input("Enter income amount: "))
                budget.add_income(amount)
            elif choice == "2":
                category = input("Enter income amount: ")
            elif choice == "3":
                budget.show_summary()
            elif choice == "4":
                budget.show_expense_breakdown()
            elif choice == "5":
                print("Exciting Budget Tracker. Enjoy your Day!")
            else:
                print("Invalid option. Please try again.")
                
    if __name__ == "__main__":
        main()               