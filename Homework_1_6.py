first_day_km = int(input('Введите число километров в первый день - '))
target_n_km = int(input('Введите целевое число километров - '))
current_n_km = first_day_km
n_days = 1
print(f'{n_days}-й день: {current_n_km}')
while current_n_km < target_n_km:
    current_n_km = round(current_n_km * 1.1, 2)
    n_days += 1
    print(f'{n_days}-й день: {current_n_km}')

print(f'Ответ: на {n_days}-й день спортсмен достиг результата — не менее {target_n_km} км')