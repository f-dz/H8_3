# Object-Oriented Programming (OOP) in Python

# How to Define a Class
class Dog:
    pass

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate an Object in Python
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# Instance Methods
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)

print(miles.description())

print(miles.speak("Woof Woof"))

print(miles.speak("Bow Wow"))

# Inherit From Other Classes in Python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))

# Parent Classes vs Child Classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"to create instance :: Dog(name={self.name}, age={self.age}) #REPR"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3, 20)
jim = Bulldog("Jim", 5, 15)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

# Extend the Functionality of a Parent Class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
print(miles.speak("Grrr"))

print(miles.__dict__)
print(buddy.__dict__)
print(jack.__dict__)
print(jim.__dict__)

print(repr(miles))