class Farm : 
    def __init__(self, farm_name):
        self.farm = farm_name
        self.all_animals = {}
    
    def add_animal(self, name_animal, amount = 1):
        if name_animal in self.all_animals :
            self.all_animals[name_animal] += amount
        else :
            self.all_animals[name_animal] = amount

    def get_info(self) :
        sentence = f"\n{self.farm} Farm \n \n"
        for animal, amount in self.all_animals.items() :
           sentence += f"{animal} : {amount} \n"
        sentence += "\n \t E-I-E-I-0!"
        return sentence
    
    def get_animal_types(self) :
        all_keys = list(self.all_animals.keys())
        return sorted(all_keys) 

    def get_short_info(self) :
        all_keys_animals = self.get_animal_types()
        for animal, amount in self.all_animals.items() :
            if amount > 1 :
                position_animal = all_keys_animals.index(animal)
                all_keys_animals[position_animal] += "s"

        joining_animals = ", ".join(all_keys_animals[:-1]) 
        sentence = f"\n{self.farm} Farm has {joining_animals} and {all_keys_animals[-1]}"
        print(sentence)




macdonald = Farm("Mc Donald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('snake')
macdonald.add_animal('goat', 12)
print(macdonald.get_animal_types())
macdonald.get_short_info()