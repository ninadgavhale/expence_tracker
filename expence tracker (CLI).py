store = []

def expence_tracker():
    while True:
        user_expence = float(input(" amount you spend "))
        description = input("describe , where u spend  ")
        store.append({
            "ammount":user_expence,
            "description":description
        })
        
        another = input("do you want to add another expence? (yes/no) ").strip().lower()
        if another == 'yes':
            pass
        elif another == "no":
            print("thank you for using expence tracker")
            break
        else:            
            print("thank you for using expence tracker")
            break
    print(f"your total expence is {sum(expence['ammount'] for expence in store)}")
    

def view_expenses():
    print("your expences are :")
    for expence in store:
        print(f"{expence['description']} : {expence['ammount']}")


def delete_expenses():

    description_to_delete = input("enter the description of the expence you want to delete: ")
    deletation = None
    for expence in store:
        if expence['description'] == description_to_delete:
            deletation = expence
            break
    if deletation:
        store.remove(deletation)
        print("expence deleted successfully.")
    else:
        print("expence not found.")

expence_tracker()
view_expenses()
delete_expenses()
print(store)
