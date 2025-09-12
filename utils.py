class Person:
    def __init__(self,fullname,username,age,phonenumber):
        self.fullname=fullname
        self.username=username
        self.age=age
        self.phonenumber=phonenumber

    def __str__(self):
        return f"Name: '{self.fullname}', username: '{self.username}', Age: '{self.age}', Phone Number: '{self.phonenumber}'"

class Product:
    def __init__(self, name, category, price, quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
    
    def update_price(self,price):
        self.price=price



    

# icecream=Product("Vanilla Icecream","Food",100,20)
# print(icecream.name)
# print(icecream.category)
# print(icecream.price)
# print(icecream.quantity)
# icecream.update_price(120)
# print(icecream.price)

# pratul=Person("Pratul Kumar","Pratul74",22,"7004644521")
# print(pratul)
    