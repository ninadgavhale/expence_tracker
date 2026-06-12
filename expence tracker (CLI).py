store = []

def expence_tracker():
    while True:
        user_expense= float(input(" amount you spend "))
        description = input("describe , where u spend  ")
        store.append({
            "ammount":user_expense,
            "description":description
        })
        
        another = input("do you want to add another expence? (yes/no) ").strip().lower()
        if another == 'yes':
            pass
        elif another == "no":             # there is no need to check for "no" because if it's not "yes" it will automatically go to the else block, but i added it for better readability
            print("thank you for using expence tracker") 
            break
        else:            
            print("thank you for using expence tracker")
            break
    print(f"your total expence is {sum(expense['ammount'] for expense in store)}")  # 
    

def view_expenses(): 
    print("your expences are :")
    for expense in store:
        print(f"{expense['description']} : {expense['ammount']}")


def delete_expenses():

    description_to_delete = input("enter the description of the expense you want to delete: ")
    deletation = None
    for expense in store:
        if expense['description'] == description_to_delete:
            deletation = expense
            break
    if deletation:
        store.remove(deletation)
        print("expense deleted successfully.")
    else:
        print("expense not found.")

# def show_total_expenses():
#     total_amount = 0
#     for expences in store:
#         if expences['ammount']:
#             total_amount += expences['ammount']
#     print(f"Total expenses: {total_amount}")
            

def show_total_expenses():
    total_amount = 0

    for expense in store:
        total_amount += expense['ammount']

    print(f"Total expenses: {total_amount}")

# def show_total():
#     total = sum(expense['amount'] for expense in store)
#     print(f"Total expenses: {total}")
 


# expence_tracker()
# view_expenses()
# delete_expenses()
# show_total_expenses()
# print(store)

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            expence_tracker()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expenses()
        elif choice == '4':
            show_total_expenses()
        elif choice == '5':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")