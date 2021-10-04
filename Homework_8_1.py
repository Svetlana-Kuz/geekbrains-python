class Date:

    def __init__(self, date: str):
        Date.date = date

    @classmethod
    def transform(cls, date):
        new_date = date.split('-')
        day = int(new_date[0])
        month = int(new_date[1])
        year = int(new_date[2])
        return day, month, year


    @staticmethod
    def valid(date):
        d, m, y = Date.transform(date)
        if 0 < d < 32:
            if 0 < m < 13:
                if 1899 < y < 2022:
                    return print('Дата введена корректно')
                else:
                    return print('Введен некорректный год (д.б. от 1900 до 2021)')
            else:
                return print('Введен некорректный месяц')
        else:
            return print('Введен некорректный день')

d, m, y = Date.transform('31-12-2021')
print(d, m, y)
# date = Date('31-12-2021')
# d, m, y = date.transform('31-12-2021')
# print(d, m, y)
Date.valid('28-6-2022')