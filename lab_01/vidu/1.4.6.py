#đa hình ở thời điểm biên dịch
#Overloading(nạp chồng)
class Caculation:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c

#overloading (ghi đè)
class Animal:
    def make_sound(self):
        return "Generic sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof!"