from menu_item import MenuItem

tax_rate = 0.0875

class Order: 
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, index):
        if 1 <= index <= len(self.items):
            self.item.pop(index - 1)
        else:
            print("Invalid item number.")
    
    def subtotal(self):
        return sum(item.price for item in self.items)
    
    def tax(self):
        return self.subtotal() + self.tax()
    
    def total(self):
        return self.subtotal() + self.tax()
    
    def __str__(self):
        receipt = "\n**** Starlight Coffee Receipt ****\n"
        receipt += f"Customer: {self.customer_name}\n\n"

        for i, item in enumerate(self.items, start=1):
            receipt += f"{i}. {item}\n"
        
        receipt += "\n"
        receipt += f"Subtotal: ${self.subtotal():.2f}\n"
        receipt += f"Tax (8.75%): ${self.tax():.2f}\n"
        receipt += f"Total: ${self.total():.2f}\n"
        receipt += "\n" + "*" *32 + "\n"

        return receipt