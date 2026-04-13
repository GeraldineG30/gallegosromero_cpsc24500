class MenuItem:
    
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.size}) - ${self.price:.2f}"
    
