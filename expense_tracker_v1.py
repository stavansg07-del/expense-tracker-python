#Expense Tracker Project 1
expenses=[]
def add_expense():
    category=input("Enter the category:")
    amount=int(input("Enter the amount:"))
    expenses.append([category,amount])
    print(expenses)

def view_expense():
    if not expenses:
        print("No record found ")
    else:
        for expense in expenses:
            print(expense[0],expense[1])

def show_total():
    total=0
    for amount in expenses:
        total+=amount[1]
    print("Total expense:",total)

def delete_expense():
    delete=input("Enter category:")
    for expense in expenses:
        if delete==expense[0]:
            expenses.remove(expense)
            print("Deleted Sucessfully!")
            break
        else:
            print("Category not found")
            
def menu():
    while True:
        print("--------Expense Tracker--------")
        print("1.Add expense")
        print("2.View expense")
        print("3.Total expense")
        print("4.Delete expense")
        print("5.Exit")

        choice=input("Enter choice:")
        if choice=='1':
            add_expense()
        elif choice=='2':
            view_expense()
        elif choice=='3':
            show_total()
        elif choice=='4':
            delete_expense()
        elif choice=='5':
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")
menu()







