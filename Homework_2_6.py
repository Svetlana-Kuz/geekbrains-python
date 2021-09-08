goods = list()
n = 1
i = 1
about_good = dict()
while n == 1:
    about_good['название'] = input('Введите название товара - ')
    about_good['цена'] = input('Введите цену товара - ')
    about_good['количество'] = input('Введите количество товара - ')
    about_good['ед'] = input('Введите единицы измерения товара - ')
    num_good = (i, about_good)
    goods.append(num_good)
    n = int(input('Ввести еще товар? 0 - нет, 1 - да  '))
    if n == 1:
        i += 1
j = 0
name = []
price = []
num = []
unit = []
while j < i:
    # name.append(goods[j](1).setdefault('название'))
    print(goods[0])
    j +=1
print(name)


