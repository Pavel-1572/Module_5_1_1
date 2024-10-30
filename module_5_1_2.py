class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name


h1 = House('Название: ЖК Эльбрус, кол-во этажей 10', 10)
h2 = House('Название: ЖК Акация, кол-во этажей 20', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
