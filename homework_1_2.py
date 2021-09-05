SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
time_second = int(input('Введите время в секундах - '))
hours = time_second // SECONDS_IN_HOUR
seconds_without_hours = time_second - hours * SECONDS_IN_HOUR
minutes = seconds_without_hours // SECONDS_IN_MINUTE
seconds = seconds_without_hours % SECONDS_IN_MINUTE
print('Введенное время в часах, минутах и секундах составляет {}:{}:{}'.format(hours, minutes, seconds))