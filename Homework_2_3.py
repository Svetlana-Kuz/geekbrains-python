month = input('Введите целое число от 1 до 12 - ')
winter = ['12', '1', '2']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']
for m in winter:
    if month == m:
        print('Это зима')
for m in spring:
    if month == m:
        print('Это весна')
for m in summer:
    if month == m:
        print('Это лето')
for m in autumn:
    if month == m:
        print('Это осень')
if int(month) > 12 or int(month) < 1:
    print('Такого месяца не существует')

month = int(input('Введите целое число от 1 до 12 - '))
seasons = {1: 'зима',
           2: 'зима',
           3: 'весна',
           4: 'весна',
           5: 'весна',
           6: 'лето',
           7: 'лето',
           8: 'лето',
           9: 'осень',
           10: 'осень',
           11: 'осень',
           12: 'зима'}
print('Это', seasons[month])
if int(month) > 12 or int(month) < 1:
    print('Такого месяца не существует')