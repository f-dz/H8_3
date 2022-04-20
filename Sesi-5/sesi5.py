# OBJECT ORIENTED PROGRAMMING

# Class
print('=====CLASS=====')

class Flower:
    size = 'medium'
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def description(self):
        return f"A {self.color} {self.name} is beautiful"
    def has_color(self, value):
        if (value == True):
            return f"{self.name} has many colors"
        elif(value==False):
            return f"{self.name} has one color"

flower1 = Flower('Rose', 'red')
flower2 = Flower('Jasmine', 'white')
flower2.size = 'small'
print(flower1.name, flower1.color, flower1.size)
print(flower2.name, flower2.color, flower2.size)
print('description :', flower1.description())
print('description :', flower2.description())
print('has color :', flower1.has_color(True))
print('has color :', flower2.has_color(False))


# Inheritance
print('=====INHERITANCE=====')

class SmallFlower(Flower):
    size = 'small'

class MediumFlower(Flower):
    size = 'medium'

class BigFlower(Flower):
    size = 'big'
    def description(self):
        return f"A {self.color} {self.name} is a big flower"

flower3 = BigFlower('Sunflower', 'yellow')
print(flower3.name, flower3.color, flower3.size)
print('description :', flower3.description())
print('has color :', flower3.has_color(False))

print(flower1.__dict__)
print(flower2.__dict__)
print(flower3.__dict__)