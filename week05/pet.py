# Geraldine Gallegos Romero     4/26/2026
# This simulator demostrates inheritance and polumorphism.
# It allows you yo interact with different types of pets. 

# Base class
class Pet:
    def __init__(self, name, species):
        self._name = name
        self._species = species
        self._hunger = 50
        self._happiness = 50
        self._energy = 50

        @property
        def name(self):
            return self._name
        
        def feed(self):
            self._hunger = max(0, self._hunger - 10)
            return f"{self._name} was fed"
        
        def play(self):         # This has to prevent values for going below 0, isn't it? ':3
            self._happiness = max(0, self._happiness + 10)
            self._energy = max(0, self._energy - 10)
            return f"{self._name} is playing"
        
        def sleep(self):
            self._energy = max(0, self._energy + 10)
            return f"{self._name} is sleeping"
        
        def status(self):
            return (f"{self._name} ({self._species})"
                    f"Hunger: {self._hunger}, "
                    f"Happiness: {self._happiness}, "
                    f"Energy: {self._energy}")
        
        def __str__(self):
            return f"{self._name} the {self._species}"
        
        
        
        
