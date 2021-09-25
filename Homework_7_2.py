from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Clothes):

    def __init__(self, name, v:int):
        super().__init__(name)
        self.v = v

    @property
    def tissue_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, h: float):
        super().__init__(name)
        self.h = h

    @property
    def tissue_consumption(self):
        return self.h * 2 + 0.3


my_coat = Coat('Моё пальто', 44)
my_suit = Suit('Мой костюм', 1.75)

print(round(my_suit.tissue_consumption, 2))
print(round(my_coat.tissue_consumption, 2))