class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print("Price:", self.price, "Max Speed:", self.max_speed, "Total Miles:", self.miles)
        return self
    
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self


bmx = Bike(500, "30mph")
bmx.ride().ride().ride().reverse().displayInfo()
mountain = Bike(400, "23mph")
mountain.ride().ride().reverse().reverse().displayInfo()
trail = Bike(200, "15mph")
trail.reverse().reverse().reverse().displayInfo()