all_item=[]
def add_item():

    try:
        item_name=input("Name of Item: ")
        item_quantity=int(input("Total item: "))
        item_price=int(input("Item price: "))
        dict1={
        "name":item_name,
        "quantity":item_quantity,
        "price":item_price,
        }
        all_item.append(dict1)
    except:
        print("\nPlease Input Integer Number and String for Item Name")
    
    

def view_item():

    if len(all_item)==0:
        print("\nPlease add your item into view.")
        
    else:
        print("\nView cart contents")
        print("--------------------")
        for i in range(0,len(all_item)):
           print(f"Item Name: {all_item[i]["name"]}  Quantity: {all_item[i]["quantity"]} Each Item Price: {all_item[i]["price"]}")
        

def total_price():

    print("\nItem Detials")
    print("-------------")
    if len(all_item)==0:
        print("No Item in View!")
    else:
        total=0
        for i in range(0,len(all_item)):
            total+=all_item[i]["quantity"]*all_item[i]["price"]
            print(f"Name: {all_item[i]["name"]}  Quantity: {all_item[i]["quantity"]}   Price: {all_item[i]["quantity"]*all_item[i]["price"]}")
        
        print("----------------------------------------")

        if total>1000:
            discount=(10*total)/100.0
            print("Total Price:       ",total)
            print("Disconts 10%:      ",discount)
            print("Final Total Price: ",total-discount)
        else:
            print("No Discount!")
            print("Final Total Price: ",total)
           

def clear_view():

    if len(all_item)==0:
        print("\nNo item in view.")
    else:
        all_item.clear()

while True:

    manu="""
    ==== Menu ====
    1. Add item
    2. View Cart
    3. Total Price for item
    4. Clear View Cart
    5. Exit
    ======****=======
    """
    print(manu)

    try:
        
        n=int(input("Enter your option: "))
        if n==5:
            break
        elif n==4:
            clear_view()
        elif n==1:
            add_item()
        elif n==2:
            view_item()
        elif n==3:
            total_price()
        else:
            print("\nPlease press only 1-5!")
    except:
        print("\nPlease press only 1-5!")

