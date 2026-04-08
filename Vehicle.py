# SUPER CLASS
class Vehicle:
    def __init__(self, brand: str):
        # Attribute common to all vehicles
        self.brand = brand

    def start_engine(self):
        # Generic engine start method
        print(f"{self.brand} vehicle is starting...")

# SUB CLASS: CAR
class Car(Vehicle):
    def __init__(self, brand: str, doors: int):
        # Use super() to initialize attributes from the parent class
        super().__init__(brand)
        self.doors = doors  # Additional attribute specific to Car
    
    def start_engine(self):
        # Overriding the parent method
        # Optionally call the parent method using super()
        super().start_engine()
        print(f"{self.brand} car engine starts with a key or push button.")


class Motorcycle(Vehicle):
    def __init__(self, brand: str,  type: str):
        # Use super() to initialize parent attributes
        super().__init__(brand)
        self.type = type  # Additional attribute specific to Motorcycle

    def start_engine(self):
        super().start_engine()
        print(f"{self.brand} motorcycle engine starts with a kick or electric start.")

# Demonstration of method overriding
# Create objects
car = Car("Toyota", 4)
motorcycle = Motorcycle("Yamaha", "Sport")

# Call start_engine() on both objects
print("Car: ")
car.start_engine()

print("\nMotorcycle:")
motorcycle.start_engine()
