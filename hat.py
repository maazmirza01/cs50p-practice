import random

class Hat:

    # class variable houses no need for self.houses
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Harry") 