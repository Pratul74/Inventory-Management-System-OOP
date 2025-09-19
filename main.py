from utils import Product, Inventory


if __name__=="__main__":
    options=["A. Add New Item","B. View Inventory","C. Update Item","D. Remove Item","E. Generate Reports","F. Exit"]
    switch_on=True
    newInventory=Inventory()
    while switch_on:
        for option in options:
            print(option)
        user=input("Select Option: ")
        if user.upper()=="F":
            switch_on=False

        elif user.upper()=="A":
            p_name=input("Enter your product name: ")
            p_price=int(input(f"Enter {p_name}'s price: "))
            p_category=input(f"Enter {p_name}'s category: ")
            p_quantity=input(f"Enter the quantity of {p_name}: ")
            newproduct=Product(name=p_name,category=p_category,price=p_price,quantity=p_quantity)
            success=newInventory.add_product(newproduct)
            if success:
                print("Product Added successfully :)")
            else:
                print("Error!")
        elif user.upper()=="B":
            print(newInventory)

        elif user.upper()=="C":
            subOptions=["A. Update Category","B. Update Price","C. Update Quantity"]
            for subOption in subOptions:
                print(subOption)
            user_answer=input("Select Option: ")
            if user_answer=="A":
                product_name=input("Enter the product name you want to change the category: ")
                newInventory.update_category()



        
            
