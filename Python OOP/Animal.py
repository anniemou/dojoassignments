class Animal(object):
    def _init_(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "The health is", self.health
        return self

class Dog(Animal):
    def _init_(self):
        self.health = 150
    def pet(self):
        self.health += 5
        return self
    
class Dragon(Animal):
    def _init_(self):
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

zwo = Animal("Frostie", 100)
zwo.walk().walk().walk().run().run().displayHealth()

dog = Dog()
dog.walk().walk().walk().run().run().pet().displayHealth()

animal = Animal("Frostie", 100)
animal.pet()
animal.fly()
animal.displayHealth()