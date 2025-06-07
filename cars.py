class BMW:
    def start_engine(self):
        print("BMW engine started with a smooth rumble.")

class Ferrari:
    def start_engine(self):
        print("Ferrari engine roared to life with power!")

def start_car(car):
    car.start_engine()

if __name__ == "__main__":
    b = BMW()
    f = Ferrari()

    start_car(b)
    start_car(f)
