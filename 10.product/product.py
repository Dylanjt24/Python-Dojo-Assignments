class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, amount):
        return self.price + (self.price * amount)
    
    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
        elif reason_for_return == "like new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self. price -= (self.price * .20)
        else:
            print("Please provide a valid reason for item return.")
        return self
    
    def displayInfo(self):
        print("Price: $" + str(self.price), "\nItem Name:", self.item_name, "\nWeight:", self.weight, "\nBrand", self.brand, "\nStatus:", self.status)
        return self