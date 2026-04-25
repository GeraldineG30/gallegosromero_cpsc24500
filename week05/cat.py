from pet import Pet

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def feed(self):
        self._hunger = max(0, self._hunger - 2)        
        return f"{self._name} is licking it's paws after a delicious meal"
    
    def play(self):
        self._happiness = max(0, self._happiness + 50)
        self._energy = max(0, self._energy - 55)
        return f"{self._name} is chasing a mouse"
    
    def purr(self):
        return f"{self._name} is making biscuits...will they be gluten free?"