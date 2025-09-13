class Staff:
    def __init__(self, fullname, username, staffId, age, phonenumber):
        self.fullname=fullname
        self.username=username
        self.age=age
        self.phonenumber=phonenumber
        self.staffId=staffId


    def __str__(self):
        return f"Name: '{self.fullname}', username: '{self.username}', Staff Id: '{self.staffId}', Age: '{self.age}', Phone Number: '{self.phonenumber}'"

class Product:
    def __init__(self, name, category, price, quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
    
    def update_price(self,price):
        self.price=price


class Inventory:

    def add_staff(self):
        pass

    def add_product(self):
        pass

    def __str__(self):
        pass




    
    



    

# icecream=Product("Vanilla Icecream","Food",100,20)
# print(icecream.name)
# print(icecream.category)
# print(icecream.price)
# print(icecream.quantity)
# icecream.update_price(120)
# print(icecream.price)

# pratul=Staff("Pratul Kumar",101,"Pratul74",22,"7004644521")
# inventory=Inventory(pratul,icecream)
# inventory.add_supply(icecream,500)

    