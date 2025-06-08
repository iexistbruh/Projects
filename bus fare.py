class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100 
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()

    bus = Bus(50) 
    print("Total Bus Fare:", bus.fare())
