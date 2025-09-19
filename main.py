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
                new_category=input("Enter the new category: ")
                success_cat_change=newInventory.update_category(product_name=product_name,new_category=new_category)
                if success_cat_change:
                    print(f"Category changed successfully")
                else:
                    print("Error!")
            elif user_answer=="B":
                product_name=input("Enter the product name you want to change the price: ")
                new_price=input("Enter the new price: ")
                price_change_success=newInventory.update_price(product_name=product_name,newPrice=new_price)
                if price_change_success:
                    print("Price Changed successfully :)")
                else:
                    print("Error!")
            elif user_answer=="C":
                product_name=input("Enter the product name you want to change the price: ")
                additional_quantity=input("Enter new quantity you want to add in inventory: ")
                quantity_change_success=newInventory.update_stock(product_name=product_name,new_quantity=additional_quantity)
                if quantity_change_success:
                    print("Quantity added successfully :)")
                else:
                    print("Error!")
            else:
                print("You entered wrong choice, Try again")
                continue





        
            
