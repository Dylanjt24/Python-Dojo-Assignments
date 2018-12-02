class MathDojo:
    def __init__(self):
        self.total = 0
    def add(self, *args):
        for num in args:
            self.total += num
        return self
    def subtract(self, *args):
        for num in args:
            self.total -= num
        return self
    def result(self):
        return self.total

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)