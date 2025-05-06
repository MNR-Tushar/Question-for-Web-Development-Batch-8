
All_Item={}
All_price={}

def add_item():
    
    try:
        name=input("Item Name: ")
        while name.isdigit():
            print("Please input valid item name.")
            name=input("Item Name: ")
        
        name=name.lower()
        name=name.capitalize()

        quantity=int(input("Quantity: "))
        while quantity<=0:
            print("Please input Quantity grather than 0")
            quantity=int(input("Quantity: "))

        price=int(input("Unit price: "))
        while price<=0:
            print("Please input Price grather than 0")
            price=int(input("Unit price: "))

        x=All_Item.get(name)
        total=price*quantity
        if x==None:
            All_Item[name]=quantity
            All_price[name]=total
        else:
            All_Item[name]+=quantity
            All_price[name]+=total
    except:
        print("\nInvalid Input")

def view_item():

    if len(All_Item)==0:
        print("\nNo Item in View!")
    else:
        print("\nGroup by all item")
        for i in All_Item:
            print(f"{i} -> Quantity: {All_Item.get(i)}")


def total_revenue():
    if len(All_Item)==0:
        print("\nNo Item in View!")
    else:
        for i in All_Item:
            print("\nItem: ",i)
            print("Total Quantity Sold: ",All_Item.get(i))
            print("Total Revenue: ",All_price[i])
    
def clear_item():
    if len(All_Item)==0:
        print("\nNo Item in View!")
    else:
        All_price.clear()
        All_Item.clear()
        print("\nAll Item clear in View!")

while True:

    manu="""
Daily Sales Report Generator
    ---- Manu -----
    1. Add Item       
    2. View Item      
    3. Total Revenue  
    4. Clear All Item    
    5. Exit           
    ------*_*--------
    """
    print(manu)

    try:
        n=int(input("Enter Your Option: "))
        if n==1:
            add_item()
        elif n==2:
            view_item()
        elif n==3:
            total_revenue()
        elif n==4:
            clear_item()
        elif n==5:
            break
        else:
            print("\nInvalid Input. Press 1-5")
    except:
        print("\nInvalid Input. Try again!")
