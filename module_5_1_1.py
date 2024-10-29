class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.say_info()

    def say_info(self):
        print(f'{self.name}, {self.number_of_floors}')

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

h1 = House('ЖК "Пушкинские горизонты"', 15)
h2 = House('ЖК "Сибиряков"', 21)

h1.go_to(7)
h2.go_to(25)
