class Furniture:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class House:
    def __init__(self, address, size):
        self.address = address
        self.size = size
        self.free_size = size
        self.furniture = []

    def __str__(self):
        return "the location is {}, the size is {}, the free size is {} and the furniture include {}".format(self.address, self.size, self.free_size, self.furniture)

    def add_furniture(self, item):
        if self.free_size > item.size:
            self.furniture.append(item.name)
            self.free_size -= item.size

        else:
            print("the furniture is too big to place")

bed = Furniture("bed1", 5)
sofa = Furniture("sofa1", 4)

home1 = House("Melbourne", 656)
print(home1)

home1.add_furniture(bed)
home1.add_furniture(sofa)
print(home1)