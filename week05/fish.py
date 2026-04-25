from pet import Pet

class Fish(Pet):
    def __init__(self, name):
        super().__init__(name, "Fish")

    def feed(self):
        self._hunger = max(0, self._hunger - 5)
        # self._happiness += 5 ... does fish get happier after eating?
        return f"{self._name} Glub...Glub...Glub"
    
    def play(self): # Not sure if a fish can play though...
        self._happiness = max(100, self._happiness + 1)
        self._energy = max(0, self._energy - 55)
        return f"{self._name} is swimming happily"
    
    def sleep(self):
        self._energy = max(0, self._energy + 25)
        return f"{self._name} is sleeping...let's check if it's a secret fairy odd parent"