class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, quantity=1):
        if animal in self.animals:
            self.animals[animal] += quantity
        else:
            self.animals[animal] = quantity

    def get_animal_types(self):
        animal_types = sorted(self.animals.keys())
        return animal_types

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_types_str = ', '.join(animal_types)
        output = f"{self.name}'s farm has {animal_types_str}."
        return output

    def get_info(self):
        animal_types = self.get_animal_types()
        max_animal_type_length = max(len(animal_type) for animal_type in animal_types)

        output = f"{self.name}'s farm\n\n"
        for animal, quantity in self.animals.items():
            output += f"{animal.ljust(max_animal_type_length)} : {quantity}\n"
        output += "\nE-I-E-I-0!"
        return output


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_short_info())





    

