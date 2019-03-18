from math import trunc

""""
ДЗ 2
На вход принимаем: Имя, Возраст, пол, рост, вес
Вычисляем BMI
Выводим: Приветствие: Уважаемая(й) <Имя> Ваш возраст: Ваш рост: Ваш вест Ваш BMI

Рекомендации:

 - Пол
 - Возраст
 - Рост
 - Вес
 <Рекомендация>
 График BMI
 0############34__________x__67**************83---------


 Интерпретация  показателя BMI ВОЗ:
 В соответствии с рекомендациями ВОЗ разработана следующая интерпретация показателей ИМТ[1]:

Индекс массы тела	Соответствие между массой человека и его ростом
16 и менее	Выраженный дефицит массы тела
16—18,5	Недостаточная (дефицит) масса тела
18,5—24,99	Норма
25—30	Избыточная масса тела (предожирение)
30—35	Ожирение
35—40	Ожирение резкое
40 и более	Очень резкое ожирение

"""
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


def bmi_adult(bmi_local):
    weight_rec1 = scale[0] * (height / 100) ** 2
    weight_rec2 = scale[1] * (height / 100) ** 2
    weight_rec3 = scale[2] * (height / 100) ** 2
    weight_rec4 = scale[3] * (height / 100) ** 2
    graph_bmi = '#' * 10 + '_' * 5 + '-' * 12 + '*' * 10 + '+' * 5
    if bmi_local <= scale[0]:
        print('Выраженный дефицит массы тела. Обратитесь к специалисту.')
        index = trunc(weight / (weight_rec1 + 0.01) * 10)
    elif bmi_local < scale[1]:
        print('Недостаточная (дефицит) масса тела. Скорректируйте питание.')
        index = trunc((weight - weight_rec1) / (weight_rec2 - weight_rec1 + 0.01) * 5) + 10
    elif bmi_local < scale[2]:
        print('Ваш вес в норме (по методике ВОЗ).')
        index = trunc((weight - weight_rec2) / (weight_rec3 - weight_rec2 + 0.01) * 12) + 15
    elif bmi_local < scale[3]:
        print('Ожирение. Скорректируйте питание.')
        index = trunc((weight - weight_rec3) / (weight_rec4 - weight_rec3 + 0.01) * 10) + 27
    else:
        print('Ожирение резкое. Обратитесь к специалисту.')
        index = 37 + trunc((weight - weight_rec2) * 10 / weight_rec2)
        if index > 40:
            index = 40
    graph_bmi = graph_bmi[:index] + 'x' + graph_bmi[index + 1:]
    graph_bmi = '0' + graph_bmi[:10] + str(round(weight_rec1)) + graph_bmi[10:15] + \
                str(round(weight_rec2)) + graph_bmi[15:27] + str(round(weight_rec3)) + \
                graph_bmi[27:37] + str(round(weight_rec4)) + graph_bmi[37:]
    print('Ваш вес находится в позиции x на диаграмме веса для вашего роста:')
    print(graph_bmi)


def bmi_child(age_, sex_, weight_):
    weight_rec1 = (bmiDict[(age_, sex_)] - 2) * (height / 100) ** 2
    weight_rec2 = (bmiDict[(age_, sex_)] + 2) * (height / 100) ** 2
    graph_bmi = '#' * 10 + '-' * 12 + '*' * 10
    if weight_ < weight_rec1:
        print('Недостаточная (дефицит) масса тела.')
        index = trunc(weight_ / (weight_rec1 + 0.01) * 10)
    elif weight_ < weight_rec2:
        print('Ваш вес в норме.')
        index = trunc((weight_ - weight_rec1) / (weight_rec2 - weight_rec1 + 0.01) * 12) + 10
    else:
        print('Избыточный вес')
        index = 22 + trunc((weight_ - weight_rec2) * 10 / weight_rec2)
        if index > 30:
            index = 30
    graph_bmi = graph_bmi[:index] + 'x' + graph_bmi[index + 1:]
    graph_bmi = '0' + graph_bmi[:10] + str(round(weight_rec1)) + graph_bmi[10:22] + \
                str(round(weight_rec2)) + graph_bmi[22:32]
    print('Ваш вес находится в позиции x на диаграмме веса для вашего роста:')
    print(graph_bmi)


def bmi_advice(age_, sex_, weight_, bmi_):
    if age_ >= 18:
        # расчет веса человека в зависимости от роста и рекомендаций ВОЗ.
        # Формирование шкалы.
        bmi_adult(bmi_)
    elif age >= 6:
        bmi_child(age_, sex_, weight_)


def bmi_greeting(f_name_, sex_, age_, height_, weight_, bmi_):
    greeting = 'Уважаемый ' if sex_ == 'м' else 'Уважаемая '
    greeting += f_name_ + '\nВаш возраст: ' + str(age_) + '\nВаш рост: ' + str(height_) + '\nВаш вес: ' + str(
        weight_) + '\nВаш BMI: ' + str(bmi_)
    print(greeting)


fName = input('Введите имя: ')
sex = input('Укажите пол (м - мужской, ж - женский): ').lower()
age = int(input('Укажите возраст: '))
height = float(input('Введите рост в сантиметрах: '))
weight = float(input('Введите вес в кг: '))
bmi = round(weight / (height / 100) ** 2, 2)
bmi_greeting()
bmi_advice(age, sex, weight, bmi)
