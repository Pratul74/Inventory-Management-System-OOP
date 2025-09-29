class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

    def update_price(self, price):
        self.price = float(price)

    def add_quantity(self, new_quantity):
        self.quantity += int(new_quantity)

    def update_category(self, new_category):
        self.category = new_category


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for p in self.products:
            if p.name.lower() == product.name.lower():
                return False  # Prevent duplicates by name
        self.products.append(product)
        return True

    def update_stock(self, product_name, new_quantity):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                product.add_quantity(new_quantity)
                return True
        return False

    def update_category(self, product_name, new_category):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                product.update_category(new_category)
                return True
        return False

    def delete_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                return True
        return False

    def update_price(self, product_name, new_price):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                product.update_price(new_price)
                return True
        return False

    def get_total_value(self):
        return sum(product.price * product.quantity for product in self.products)

    def get_category_summary(self):
        summary = {}
        for product in self.products:
            summary[product.category] = summary.get(product.category, 0) + 1
        return summary

    def get_low_stock(self, threshold=5):
        return [p for p in self.products if p.quantity < threshold]

    def __str__(self):
        if not self.products:
            return "Inventory is empty."
        product_list = "Product Inventory:\n"
        product_list += "-" * 70 + "\n"
        for product in self.products:
            product_list += (
                f"{product.name:<15} | "
                f"Category: {product.category:<12} | "
                f"Price: {product.price:<8.2f} | "
                f"Quantity: {product.quantity}\n"
            )
        return product_list








    
    



    
