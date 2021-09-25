class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        self.__string = []
        for i in self.lists:
            i = ' '.join(str(el) for el in i)
            self.__string.append(i)
        return '\n'.join(self.__string)

    def __add__(self, other):
        if len(self.lists) != len(other.lists) or len(self.lists[0]) != len(other.lists[0]):
            return 'Сложение невозможно, матрицы разных размеров' # по умолчанию вводятся матрицы, поэтому сравнивается количество элементов в первой строке. По идее в ините можно еще проверить, действительно ли ввенный список списков является матрицей
        else:
            new_list = [[self.lists[i][j] + other.lists[i][j] for j in range(len(self.lists[0]))] for i in range(len(self.lists))]
            new_m = Matrix(new_list)
        return new_m



list_1 = [[31, 22],
          [37, 43],
          [51, 86]]
list_2 = [[3, 5],
          [-3, 8],
          [26, 32]]
# list_3 = [[1, 1],
#           [1, 1],
#           [1, 1],
#           [1, 1]]
m1 = Matrix(list_1)
m2 = Matrix(list_2)
# m3 = Matrix(list_3)
print(m1 + m2)

