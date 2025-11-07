expenses = []
def add_expenses():
    try:
        category = input("Enter ur expenses: ").capitalize()
        amount = float(input("Enter amount which you spent: "))
        note = input("Enter the describtion: ")
        expense= {
            "category": category ,
            "amount": amount,
            "note": note
        }
        expenses.append(expense)
        print("Expenses added successfully")
    except ValueError:
        print("Invalid input, plz enter numeric value")
    except Exception as e:
        print("An expected error", e)        

def view_expenses():      
    try:
        if not expenses:
            print("No expenses found")
            return
        
        print("Your Expenses:")
        for i, exp in range(expenses,1):
            print(f"{i}. Category: {exp['category']}")
            print(f"   Amount: {exp['amount']}")
            print(f"   Note: {exp['note']}")
            total += exp['amount']
            print("-" * 40)
        print()
        print("Total expense: ", total)
    except Exception as e:
        print("An unexpected error:", e)
        
def search_category():       
    try:
        if not expenses:
            print("no expenses found")
            return
        
        category_search = input("Enter category to search: ").capitalize()
        found = [e for e in expenses if e["category"] == category_search]
        if not found:
            print(f"No expenses found for category: {category_search}\n")
            return
        for e in found:
            print(f"Rs {e["amount"]} {e["note"]}")   
    except Exception as e:
        print(" An unexpected error")

def main():
    try:
        while True:
            print("======= 💰 Expense Tracker Menu =======")
            print("1️. Add Expense")
            print("2️.View All Expenses")
            print("3️. Search Expense by Category")
            print("4️.Exit")
            print("=======================================")
            
            choice = input("Enter your choice (1-4): ")
            print()

            if choice == "1":
                add_expenses()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                search_category()
            elif choice == "4":
                print("Exiting program, Goodbye!")
                break
            else:
                print("Invalid choice, please select 1–4.\n")

    except Exception as e:
        print("⚠️ An unexpected error occurred in main():", e)

main()