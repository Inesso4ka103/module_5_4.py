class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
         print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to (self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)
