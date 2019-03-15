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

fName = input('Введите имя: ')
sex = input('Укажите пол (м - мужской, ж - женский): ').lower()
age = int(input('Укажите возраст: '))
height = float(input('Введите рост в сантиметрах: '))
weight = float(input('Введите вес в кг: '))

bmi = round(weight / (height / 100) ** 2, 2)
greeting = 'Уважаемый ' if sex == 'м' else 'Уважаемая '
greeting += fName + '\nВаш возраст: ' + str(age) + '\nВаш рост: ' + \
            str(height) + '\nВаш вес: ' + str(weight) + '\nВаш BMI: ' + \
            str(bmi)
print(greeting)

if age >= 18:
    # расчет веса человека в зависимости от роста и рекомендаций ВОЗ.
    # Формирование шкалы.
    scale = (16, 18.5, 25, 30)
    weight_rec1 = scale[0] * (height / 100) ** 2
    weight_rec2 = scale[1] * (height / 100) ** 2
    weight_rec3 = scale[2] * (height / 100) ** 2
    weight_rec4 = scale[3] * (height / 100) ** 2

    graphBMI = '#' * 10 + '_' * 5 + '-' * 12 + '*' * 10 + '+' * 5

    if bmi <= scale[0]:
        print('Выраженный дефицит массы тела. Обратитесь к специалисту.')
        index = trunc(weight / (weight_rec1 + 0.01) * 10)
    elif bmi < scale[1]:
        print('Недостаточная (дефицит) масса тела. Скорректируйте питание.')
        index = trunc((weight - weight_rec1) / (weight_rec2 - weight_rec1 + 0.01) * 5) + 10
    elif bmi < scale[2]:
        print('Ваш вес в норме (по методике ВОЗ).')
        index = trunc((weight - weight_rec2) / (weight_rec3 - weight_rec2 + 0.01) * 12) + 15
    elif bmi < scale[3]:
        print('Ожирение. Скорректируйте питание.')
        index = trunc((weight - weight_rec3) / (weight_rec4 - weight_rec3 + 0.01) * 10) + 27
    else:
        print('Ожирение резкое. Обратитесь к специалисту.')
        index = 39
    graphBMI = graphBMI[:index] + 'x' + graphBMI[index+1:]
    graphBMI = '0' + graphBMI[:10] + str(round(weight_rec1)) + graphBMI[10:15] + \
        str(round(weight_rec2)) + graphBMI[15:27] + str(round(weight_rec3)) + \
        graphBMI[27:37] + str(round(weight_rec4)) + graphBMI[37:]
elif age >= 6:
    ageIndex = age - 6
    bmiBoy = [16, 16, 16, 17, 17, 18, 19, 20, 20, 20, 20, 21]
    bmiGirl = [16, 16, 16, 17, 17, 18, 19, 20, 20, 21, 21, 21]
    if sex == 'м':
        weight_rec1 = (bmiBoy[age] - 2) * (height / 100) ** 2
        weight_rec2 = (bmiBoy[age] + 2) * (height / 100) ** 2
    else:
        weight_rec1 = (bmiGirl[age] - 2) * (height / 100) ** 2
        weight_rec2 = (bmiGirl[age] + 2) * (height / 100) ** 2
    graphBMI = '#' * 10 + '-' * 12 + '*' * 10
    if weight < weight_rec1:
        print('Недостаточная (дефицит) масса тела.')
        index = trunc(weight / (weight_rec1 + 0.01) * 10)
    elif weight < weight_rec2:
        print('Ваш вес в норме.')
        index = trunc((weight - weight_rec1) / (weight_rec2 - weight_rec1 + 0.01) * 12) + 10
    else:
        print('Избыточный вес')
        index = 22 + trunc((weight-weight_rec2) * 10 / weight_rec2)
        if index > 30:
            index = 30
    graphBMI = graphBMI[:index] + 'x' + graphBMI[index+1:]
    graphBMI = '0' + graphBMI[:10] + str(round(weight_rec1)) + graphBMI[10:22] + \
        str(round(weight_rec2)) + graphBMI[22:32]
print('Ваш вес находится в позиции x на диаграмме веса для вашего роста:')
print(graphBMI)
