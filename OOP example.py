class Animal:
    def __init__(self, name, species):
        
        def make_sound(self):
            return "some generic sound"
    
            def info(self):
                return f"{self.name} is a {self.species}."
            
            class Dog(Animal):
                def __init__(self, name, breed):
                    super().__init__(name, "Dog")
                    self.breed = breed
                    
                    def make_sound(self):
                        return "Woof! Woof!"
                    
                    def info(self):
                        return f"{self.name} is a {self.breed} {self.species}."
                    
                    class Cat(Animal):
                        def __init__(self, name, color):
                            super().__init__(name, "Cat")
                            self.color = color
                            
                    def make_sound(self):
                        return "Meow"
                    
                    dog = Dog("Harry", "Yellow Lab")
                    cat = Cat ("Luna", "Calico")
                    
                    Print(dog.info())
                    print(dog.make_sound())
                    
                    print(cat.info())
                    print(cat.make_sound())
                    