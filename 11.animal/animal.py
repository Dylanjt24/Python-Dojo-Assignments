class Animal:
    def __init__(self, name):
        self.health = 100
        self.name = name
    def walk(self):
        self.health-= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print(self.health)
        return self

scruffy = Animal("Scruffy")
scruffy.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

nova = Dog("Nova")
nova.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super().display_health()
        print("I am a Dragon")
        return self

smaug = Dragon("Smaug")
smaug.fly().display_health()

dolphin = Animal("dolphin")
dolphin.pet()
dolphin.fly()
dolphin.display_health()

nova.fly()