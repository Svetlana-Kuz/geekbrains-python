def salary(time, rate, premium):
    try:
        return print('Зарплата равна ', float(time) * float(rate) + float(premium))
    except ValueError:
        return print('Что-то ввели не то!')


salary(input('Введите отработанное время в часах '), input('Введите ставку в час '), input('Введите премию '))
