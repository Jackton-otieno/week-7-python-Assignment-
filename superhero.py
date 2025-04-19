class Superhero:
    def __init__(self, name, power, health=100):
        self.name = name
        self.power = power
        self._health = health  # Encapsulated attribute (protected with underscore)
        self._is_active = True  # Encapsulated attribute to track if superhero is active

    def use_power(self):
        if self._is_active:
            print(f"{self.name} uses their {self.power} power!")
            self._health -= 10  # Using power reduces health
            if self._health <= 0:
                self._is_active = False
                print(f"{self.name} is too weak to continue fighting!")
        else:
            print(f"{self.name} is out of action!")

    def rest(self):
        if self._is_active:
            self._health = min(100, self._health + 20)  # Resting recovers health
            print(f"{self.name} rests and recovers to {self._health} health.")
        else:
            print(f"{self.name} needs more time to recover!")

    def get_status(self):
        status = "active" if self._is_active else "out of action"
        print(f"{self.name}'s Status: Health = {self._health}, Power = {self.power}, Status = {status}")

    def reveal_identity(self):
        print(f"I am {self.name}, with the power of {self.power}!")


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, flight_speed, health=100):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed  # New attribute specific to FlyingSuperhero

    def use_power(self):  # Polymorphism: Override the base class method
        if self._is_active:
            print(f"{self.name} flies at {self.flight_speed} mph and uses {self.power} power!")
            self._health -= 15  # Flying uses more health
            if self._health <= 0:
                self._is_active = False
                print(f"{self.name} crash-lands and is out of action!")
        else:
            print(f"{self.name} is out of action and cannot fly!")

    def soar(self):  # New method specific to FlyingSuperhero
        if self._is_active:
            print(f"{self.name} soars through the sky at {self.flight_speed} mph!")
        else:
            print(f"{self.name} is too weak to fly!")