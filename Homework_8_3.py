class NotNumber(ValueError):
    def __init__(self):
        print('Вы ввели не число')

my_list = []
while True:
    try:
        num = input('Введите целое число или stop для завершения ввода: ')
        if num == 'stop':
            break
        elif num.isdigit():
            my_list.append(int(num))
        else:
            raise NotNumber
    except NotNumber:
        pass

print(my_list)