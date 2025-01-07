List_of_Items_Product_Management_System = {
    "1"  :("Fries",30,),
    "2"  :("Cake",30,),
    "3"  :("Fish Fillet",30,),
    "4"  :("Chicken",30,),
    "5"  :("Beef Whelington",30,),
    "6"  :("Steak",30,),
    "7"  :("Crispy Salmon",30,),
    "8"  :("Mashed potato",30,),
    "9"  :("Water",30,),
    "10" :("Juice",30,),
    "11" :("Lava Cake",30,),
    "12" :("Ribs",30,),
    "13" :("Iced tea",30,),
    "14" :("Iced coffee",30,),
    "15" :("Hot Coffee",30,),
    
}

def display():
    "Displayes inventory of the machine"
    print("\nValidated Items")
#For Loop
for Company,Price in List_of_Items_Product_Management_System.items():
    print(f"{Company} Price: {Price}")

    display()

def select():
    code = input("Enter the product you may want to buy"). upper()
    if code in List_of_Items_Product_Management_System:
        return code
    else:
        print("Invalid Selection, please try again")
        return None
    
display()

selected_code = None
while selected_code is None:
    selected_code = select()

