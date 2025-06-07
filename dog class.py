class Dog:
    species = "dog"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

rocky = Dog("Rocky", 5, "Labrador")
bella = Dog("Bella", 3, "German Shepherd")

print("Rocky is a {}".format(rocky.species))
print("Bella is a {}".format(bella.species))

print("{} is a {} and is {} years old.".format(rocky.name, rocky.breed, rocky.age))
print("{} is a {} and is {} years old.".format(bella.name, bella.breed, bella.age))
