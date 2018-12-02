class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.15 if self.price > 10000 else 0.12
    
    def display_all(self):
        print("Price:", self.price, "\nSpeed:", self.speed, "\nFuel:", self.fuel, "\nMileage:", str(self.mileage) + "mpg", "\nTax:", self.tax)
        return self


volkswagen = Car(20000, "140mph", "1/4 Full", 20)
volkswagen.display_all()

bmw = Car(35000, "180mph", "Full", 30)
bmw.display_all()

audi = Car(139950, "205mph", "Almost Empty", 16)
audi.display_all()

honda = Car(8000, "95mph", "Close to Full", 35)
honda.display_all()

subaru = Car(15000, "120mph", "Full", 30)
subaru.display_all()

bentley = Car(200000, "207mph", "Empty", 12)
bentley.display_all()