

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
    
    def update_stock(self, product, new_quantity):
        product.add_quantity(new_quantity)
    
    def update_category(self, product_name, new_category):
        globals()[product_name].update_category(new_category)

    def delete_product(self, product):
        self.products.remove(product)

    def update_price(self, product, newPrice):
        product.price=newPrice
        

    def __str__(self):
        product_list="Here are the product list: \n"
        for product in self.products:
            product_list+=f"{product.name} | Category: {product.category} | Price: {product.price} | Quantity: {product.quantity}\n"
        return product_list




    
    



    
