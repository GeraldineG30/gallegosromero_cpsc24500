from pet import Pet

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self._breed = breed

    def feed(self):
        self._hunger = max(0, self._hunger - 10)
        self._happiness += 5
        return f"{self._name} it's happy to eat"
    
    def play(self):
        self._happiness = min(100, self._happiness + 10)
        self._energy = max(0, self._energy - 10)
        return f"{self._name} roll around"
    
    def fetch(self):
        return f"{self._name} is a {self._breed} and it's favorite game is fetch the ball"