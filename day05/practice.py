from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def describe(self):
        return f"{self.make} {self.model} ({self.wheels()} wheels)"
    @abstractmethod
    def wheels(self):
        pass
class Car(Vehicle):
    def wheels(self):
        return 4
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    def describe(self):
        return (
            f"{self.make} {self.model} "
            f"({self.wheels()} wheels) - Capacity: {self.capacity}"
        )

    def wheels(self):
        return 6
def main():
    vehicles = [
        Car("Toyota", "Corolla"),
        Car("Anbessa", "velocity"),
        Truck("Volvo", "BYD", "25 tons"),
        Truck("Mercedes", "Isuzu", "30 tons"),
    ]

    for vehicle in vehicles:
        print(vehicle.describe())
if __name__ == "__main__":
    main()
    #this is an abstract class that cannot be instantiated directly. It serves as a blueprint for other classes.s
