earn = int(input('Введите размер выручки - '))
costs = int(input('Введите размер издержек -  '))
result = earn - costs
if result > 0:
    efficiency = result / earn
    efficiency = round(efficiency, 2)
    print(f'Компания получила прибыль {result}. Рентабельность составляет {efficiency}')
    n_workers = int(input('Введите число работников - '))
    result_of_worker = round(result / n_workers, 2)
    print('Прибыль на одного работника составляет ', result_of_worker)
else:
    print('Компания сработала с убытком ', result)