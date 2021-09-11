def about_smb(name='', surname='', year_of_birth='', city='',
              email='', phone='') -> object:
    print(name, surname, year_of_birth, city, email, phone)


about_smb(name=input('Введите имя '), surname=input('Введите фамилию '), year_of_birth=input('Введите год рождения '),
          city=input('Введите город '), email=input('Введите email '), phone=input('Введите номер телефона '))
