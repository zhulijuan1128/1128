class Ren:
    __className = "Ren"
    def __init__(self, name, money):
        self.name = name
        self.__money = money
    def say(self):
        print("I am %s ,i have %d RMB" % (self.name, self.__money))
p = Ren('hello',100)
p.say()