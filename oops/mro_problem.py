class Animal:
    def run(self):
        print("The animal is running.")

class Dog(Animal):
    def run(self):
        print('The dog is running.')

class Cat(Animal):
    def run(self):
        print("The cat is running.")

class HybridAnimal(Dog, Cat):
    def my_method(self):
        self.run()
        Cat.run(self)

obj = HybridAnimal()
obj.my_method()