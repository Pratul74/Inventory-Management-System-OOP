

class Product:
    def __init__(self, name, category, price, quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
    
    def update_price(self,price):
        self.price=price
    
    def add_quantity(self, new_quantity):
        self.quantity+=new_quantity

    def update_category(self, new_category):
        self.category=new_category


class Inventory:
    def __init__(self):
        self.products=[]

    
    def add_product(self,product):
        if product not in self.products:
            self.products.append(product)
            return True
        return False
    
    def add_stock(self, product, new_quantity):
        product.add_quantity(new_quantity)
    
    def change_category(self, product, new_category):
        product.update_category(new_category)

    def delete_product(self, product):
        self.products.remove(product)
        

    def __str__(self):
        product_list="Here are the product list: \n"
        for product in self.products:
            product_list+=f"{product.name} | Category: {product.category} | Price: {product.price} | Quantity: {product.quantity}\n"
        return product_list




    
    



    

icecream=Product("Magnum Truffle Icecream", "Food", 80, 50)
eggs=Product("Eggs","Food",196,10)
condom=Product("Manforce Extra Dotted Condom","Bodycare",99,100)
inventory=Inventory()
inventory.add_product(icecream)
inventory.add_product(eggs)
inventory.add_product(condom)
print(inventory)
print("\n")
inventory.add_stock(icecream,20)
print(inventory)
inventory.change_category(condom,"Medicine")
print("\n")
print(inventory)
print(inventory.delete_product(condom))
print("\n")
print(inventory)
print(inventory.delete_product(eggs))
    