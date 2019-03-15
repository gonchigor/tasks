
'''
Развиваем наш калькулятор BMI
Сделать калькулятор многопользовательским
При старте доступные команды:
    Вывести список пользователей(LIST)
    Добавить пользователя(ADD)
        ввод данных нового пользователя
    Удалить пользователя(DEL)
    Выбрать пользователя(SELECT)
        Введите ID/ФИО
        После ввода - отобразить хранимые данные
        Обновить информацию(ввести)
'''
users = {}

while True:
    print('\nChoose option')
    print('menu')
    print('1 - Вывести список пользователей(LIST)')
    print('2 - Добавить пользователя(ADD)')
    print('3 - Удалить пользователя(DEL)')
    print('4 - Выбрать пользователя(SELECT)')
    print('5 - выход из программы (EXIT)')
    chosen = input('Введите пункт меню:').upper()
    if chosen == '1' or chosen == 'LIST':
        print('\n'.join(users.keys()))
    elif chosen == '2' or chosen == 'ADD':
        fName = input('Введите имя: ')
        if fName in users.keys():
            print('ERROR: user already exists')
        else:
            sex = input('Укажите пол (м - мужской, ж - женский): ').lower()
            age = int(input('Укажите возраст: '))
            height = float(input('Введите рост в сантиметрах: '))
            weight = float(input('Введите вес в кг: '))
            bmi = round(weight / (height / 100) ** 2, 2)
            users[fName] = {'sex': sex,
                            'age': age,
                            'height': height,
                            'weight': weight,
                            'bmi': bmi}
    elif chosen == '3' or chosen == 'DEL':
        fName = input('Введите имя: ')
        if fName in users.keys():
            del users[fName]
            print('User', fName, 'deleted')
        else:
            print('ERROR: user doesn\'t exist')
    elif chosen == '4' or chosen == 'SELECT':
        fName = input('Введите имя: ')
        if fName in users.keys():
            print('Пол:', users[fName]['sex'])
            print('Возраст:', users[fName]['age'])
            print('Рост:', users[fName]['height'])
            print('Вес:', users[fName]['weight'])
            print('BMI:', users[fName]['bmi'])
            if input('Обновить информацию?[д/н]:').upper() == 'Д':
                sex = input('Укажите пол (м - мужской, ж - женский): ').lower()
                age = int(input('Укажите возраст: '))
                height = float(input('Введите рост в сантиметрах: '))
                weight = float(input('Введите вес в кг: '))
                bmi = round(weight / (height / 100) ** 2, 2)
                users[fName] = {'sex': sex,
                                'age': age,
                                'height': height,
                                'weight': weight,
                                'bmi': bmi}
        else:
            print('ERROR: user doesn\'t exist')
    elif chosen == '5' or chosen == 'EXIT':
        break

