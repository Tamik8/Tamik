# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

for i in goods:
    if i == 'Лампа':
        lamp_code = goods['Лампа']
        lamp_item = store[lamp_code][0]
        lamp_quantity = lamp_item['quantity']
        lamp_price = lamp_item['price']
        lamp_cost = lamp_quantity * lamp_price
        print('Лампа -', lamp_quantity, 'шт, стоимость', lamp_cost, 'руб.')
    elif i == 'Стол':
        table_code = goods['Стол']
        table_item1 = store[table_code][0]
        table_item2 = store[table_code][1]
        table_quantity1 = table_item1['quantity']
        table_quantity2 = table_item2['quantity']
        table_price1 = table_item1['price']
        table_price2 = table_item2['price']
        table_cost = table_quantity1 * table_price1 + table_quantity2 * table_price2
        print('Стол -', table_quantity1 + table_quantity2, 'шт, стоимость', table_cost, 'руб.')
    elif i == 'Диван':
        sofa_code = goods['Диван']
        sofa_item1 = store[sofa_code][0]
        sofa_item2 = store[sofa_code][1]
        sofa_quantity1 = sofa_item1['quantity']
        sofa_quantity2 = sofa_item2['quantity']
        sofa_price1 = sofa_item1['price']
        sofa_price2 = sofa_item2['price']
        sofa_cost = sofa_quantity1 * sofa_price1 + sofa_quantity2 * sofa_price2
        print('Диван -', sofa_quantity1 + sofa_quantity2, 'шт, стоимость', sofa_cost, 'руб.')
    elif i == 'Стул':
        chair_code = goods['Стул']
        chair_item1 = store[chair_code][0]
        chair_item2 = store[chair_code][1]
        chair_item3 = store[chair_code][2]
        chair_quatity1 = chair_item1['quantity']
        chair_quatity2 = chair_item2['quantity']
        chair_quatity3 = chair_item3['quantity']
        chair_price1 = chair_item1['price']
        chair_price2 = chair_item2['price']
        chair_price3 = chair_item3['price']
        chair_cost = chair_quatity1 * chair_price1 + chair_quatity2 * chair_price2 + chair_quatity3 * chair_price3
        print('Стул -', chair_quatity1 + chair_quatity2 + chair_quatity3, 'шт, стоимость', chair_cost, "руб." '\n')

for i in goods:
    code = goods[i]
    for j in store[code]:
        quantity = j['quantity']
        price = j['price']
        cost = quantity * price
        print(i, '-', quantity, 'шт, стоимость', cost, 'руб.')
