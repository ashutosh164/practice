class Coffee:
    def __init__(self):
        self.ounces = 11

    def drink(self, sip):
        self.ounces -= sip


coffee = Coffee()

while coffee.ounces != 0:
    coffee.drink(1)

print('Get shit done! ')