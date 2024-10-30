class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.say_info()

    def say_info(self):
        print(f'Название: {self.name}, Кол-во этажей: {self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(len(h1))
print(len(h2))

