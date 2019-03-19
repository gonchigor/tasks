from math import trunc
import sys
import functools

scale = (16, 18.5, 25, 30)
bmiDict = {(6, 'м'): 16,
           (7, 'м'): 16,
           (8, 'м'): 16,
           (9, 'м'): 17,
           (10, 'м'): 17,
           (11, 'м'): 18,
           (12, 'м'): 19,
           (13, 'м'): 20,
           (14, 'м'): 20,
           (15, 'м'): 20,
           (16, 'м'): 20,
           (17, 'м'): 21,
           (6, 'ж'): 16,
           (7, 'ж'): 16,
           (8, 'ж'): 16,
           (9, 'ж'): 17,
           (10, 'ж'): 17,
           (11, 'ж'): 18,
           (12, 'ж'): 19,
           (13, 'ж'): 20,
           (14, 'ж'): 20,
           (15, 'ж'): 21,
           (16, 'ж'): 21,
           (17, 'ж'): 21
           }
users = {}
login = ''
userLogin = {
    'admin': 'qwerty',
    'user': '12345'
}


def login_user():
    global login
    if login:
        return True
    while True:
        user_name = input('Имя пользователя:')
        password = input('Пароль:')
        if userLogin.get(user_name) == password:
            login = user_name
            print('Вход произведен')
            return True
        if input('Неверное имя пользователя или пароль. Продолжить? [д/н]').upper() == 'Н':
            return False


def login_required(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if login or login_user():
            return func(*args, **kwargs)
        return
    return wrapper_decorator


# логика ИМТ
def bmi_adult(user):
    weight_rec1 = scale[0] * (user['height'] / 100) ** 2
    weight_rec2 = scale[1] * (user['height'] / 100) ** 2
    weight_rec3 = scale[2] * (user['height'] / 100) ** 2
    weight_rec4 = scale[3] * (user['height'] / 100) ** 2
    graph_bmi = '#' * 10 + '_' * 5 + '-' * 12 + '*' * 10 + '+' * 5
    if user['bmi'] <= scale[0]:
        print('Выраженный дефицит массы тела. Обратитесь к специалисту.')
        index = trunc(user['weight'] / (weight_rec1 + 0.01) * 10)
    elif user['bmi'] < scale[1]:
        print('Недостаточная (дефицит) масса тела. Скорректируйте питание.')
        index = trunc((user['weight'] - weight_rec1) / (weight_rec2 - weight_rec1 + 0.01) * 5) + 10
    elif user['bmi'] < scale[2]:
        print('Ваш вес в норме (по методике ВОЗ).')
        index = trunc((user['weight'] - weight_rec2) / (weight_rec3 - weight_rec2 + 0.01) * 12) + 15
    elif user['bmi'] < scale[3]:
        print('Ожирение. Скорректируйте питание.')
        index = trunc((user['weight'] - weight_rec3) / (weight_rec4 - weight_rec3 + 0.01) * 10) + 27
    else:
        print('Ожирение резкое. Обратитесь к специалисту.')
        index = 37 + trunc((user['weight'] - weight_rec2) * 10 / weight_rec2)
        if index > 40:
            index = 40
    graph_bmi = graph_bmi[:index] + 'x' + graph_bmi[index + 1:]
    graph_bmi = '0' + graph_bmi[:10] + str(round(weight_rec1)) + graph_bmi[10:15] + \
                str(round(weight_rec2)) + graph_bmi[15:27] + str(round(weight_rec3)) + \
                graph_bmi[27:37] + str(round(weight_rec4)) + graph_bmi[37:]
    return 'Ваш вес находится в позиции x на диаграмме веса для вашего роста:' + '\n' + graph_bmi


def bmi_child(user):
    weight_rec1 = (bmiDict[(user['age'], user['sex'])] - 2) * (user['height'] / 100) ** 2
    weight_rec2 = (bmiDict[(user['age'], user['sex'])] + 2) * (user['height'] / 100) ** 2
    graph_bmi = '#' * 10 + '-' * 12 + '*' * 10
    if user['weight'] < weight_rec1:
        print('Недостаточная (дефицит) масса тела.')
        index = trunc(user['weight'] / (weight_rec1 + 0.01) * 10)
    elif user['weight'] < weight_rec2:
        print('Ваш вес в норме.')
        index = trunc((user['weight'] - weight_rec1) / (weight_rec2 - weight_rec1 + 0.01) * 12) + 10
    else:
        print('Избыточный вес')
        index = 22 + trunc((user['weight'] - weight_rec2) * 10 / weight_rec2)
        if index > 30:
            index = 30
    graph_bmi = graph_bmi[:index] + 'x' + graph_bmi[index + 1:]
    graph_bmi = '0' + graph_bmi[:10] + str(round(weight_rec1)) + graph_bmi[10:22] + \
                str(round(weight_rec2)) + graph_bmi[22:32]
    return 'Ваш вес находится в позиции x на диаграмме веса для вашего роста:' + '\n' + graph_bmi


def bmi_advice(user):
    if user['age'] >= 18:
        # расчет веса человека в зависимости от роста и рекомендаций ВОЗ.
        # Формирование шкалы.
        return bmi_adult(user)
    elif user['age'] >= 6:
        return bmi_child(user)


def bmi_greeting(f_name_, user):
    greeting = 'Уважаемый ' if user['sex'] == 'м' else 'Уважаемая '
    greeting += f_name_ + '\nВаш возраст: ' + str(user['age']) + '\nВаш рост: ' + str(
        user['height']) + '\nВаш вес: ' + str(
        user['weight']) + '\nВаш BMI: ' + str(user['bmi'])
    return greeting


# ввод и обновление данных
def input_info(f_name):
    sex_ = input('Укажите пол (м - мужской, ж - женский): ').lower()
    age_ = int(input('Укажите возраст: '))
    height_ = float(input('Введите рост в сантиметрах: '))
    weight_ = float(input('Введите вес в кг: '))
    bmi_ = round(weight_ / (height_ / 100) ** 2, 2)
    users[f_name] = {'sex': sex_,
                     'age': age_,
                     'height': height_,
                     'weight': weight_,
                     'bmi': bmi_}


# Блоки меню
@login_required
def menu_list():
    if users.keys().__len__() > 0:
        print('\n'.join(users.keys()))
    else:
        print('Список пуст')


@login_required
def menu_add():
    f_name = input('Введите имя: ')
    if f_name in users.keys():
        print('ERROR: user already exists')
    else:
        input_info(f_name)
        print(bmi_greeting(f_name, users[f_name]))
        print(bmi_advice(users[f_name]))


@login_required
def menu_del():
    f_name = input('Введите имя: ')
    if f_name in users.keys():
        del users[f_name]
        print('User', f_name, 'deleted')
    else:
        print('ERROR: user doesn\'t exist')


@login_required
def menu_select():
    f_name = input('Введите имя: ')
    if f_name in users.keys():
        print(bmi_greeting(f_name, users[f_name]))
        print(bmi_advice(users[f_name]))
        if input('Обновить информацию?[д/н]:').upper() == 'Д':
            input_info(f_name)
            print(bmi_greeting(f_name, users[f_name]))
            print(bmi_advice(users[f_name]))
    else:
        print('ERROR: user doesn\'t exist')


def main_menu():
    print('\nChoose option')
    print('menu')
    print('1 - Вывести список пользователей(LIST)')
    print('2 - Добавить пользователя(ADD)')
    print('3 - Удалить пользователя(DEL)')
    print('4 - Выбрать пользователя(SELECT)')
    print('5 - выход из программы (EXIT)')
    chosen = input('Введите пункт меню:').upper()
    if chosen == '1' or chosen == 'LIST':
        menu_list()
    elif chosen == '2' or chosen == 'ADD':
        menu_add()
    elif chosen == '3' or chosen == 'DEL':
        menu_del()
    elif chosen == '4' or chosen == 'SELECT':
        menu_select()
    elif chosen == '5' or chosen == 'EXIT':
        sys.exit(0)


def start_program():
    while True:
        main_menu()


start_program()
