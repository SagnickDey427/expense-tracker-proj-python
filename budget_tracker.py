from budget import Expense


def main():
    #taking expenses from user
    my_expense=take_user_expense()
    expense_path="budget.csv"
    save_expenses(my_expense,expense_path)
    #summarise and show the expenses
    summarise_expense(expense_path)


def take_user_expense():
    print("🎯Taking expenses from user...")
    item_name=input("✨Enter your item name:")
    item_expense=float(input("✨Enter the expense:"))
    print("Choose a catagory to put in your item:")
    catagory_list=[
        "Food",
        "Home",
        "Work",
        "Sports & Activity",
        "Study",
        "Fun",
        "Miscellaneous"
    ]
    for i,item in enumerate(catagory_list):
        print(f"{i+1}. {item}")
    while True:
        try:
            chosen_catagory=(int(input("Your option:")))-1
            if chosen_catagory in range(len(catagory_list)):
                new_expense=Expense(name=item_name,amount=item_expense,catagory=catagory_list[chosen_catagory])
                return new_expense
            else:
                print("Invalid input.Try again!:-(")
        except:
            print("Some error occured.U_U")
def save_expenses(my_expense:Expense,expense_path):
    print(f"🎯Saving expenses to {expense_path}...")
    with open(expense_path,"a") as f:
        f.write(f"{my_expense.name},{my_expense.catagory},{my_expense.amount}\n")
def summarise_expense(expense_path):
    print("🎯summarising the expenses...")
    exp_list=[]
    with open(expense_path,"r") as f:
            lines=f.readlines()
            for line in lines:
                new_line=line.strip()
                exp_list.append(new_line)
                print (f"🎯{new_line}")
    exp_dict={}
    for item in exp_list:
        a_new_list=item.split(",")
        exp_item_name,exp_item_catagory,exp_item_amount=a_new_list
        obj_exp_new=Expense(exp_item_name,exp_item_catagory,exp_item_amount)
        dict_key=f"{obj_exp_new.catagory}"
        dict_value=float(f"{obj_exp_new.amount}")
        if dict_key in exp_dict:
            exp_dict[dict_key]+=dict_value
        else:
            new_exp_dict={dict_key:dict_value}
            exp_dict.update(new_exp_dict)
    print(exp_dict)


if __name__=="__main__":
    main()