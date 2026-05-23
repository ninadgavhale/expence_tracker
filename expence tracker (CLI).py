store = []

def expence_tracker():
    while True:
        user_expence = float(input(" amount you spend "))
        description = input("describe , where u spend  ")
        store.append((user_expence, description))
        
    another = input("do you want to add another expence? (yes/no) ")
    if another.lower() != "yes":
        break
expence_tracker()
print(store)