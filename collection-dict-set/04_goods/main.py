goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

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

for i_goods in goods.keys():
    quantity = 0
    price = 0
    i_store_list = store.get(goods.get(i_goods))
    for quantity_price in i_store_list:
        quantity += quantity_price["quantity"]
        price += quantity_price["quantity"] * quantity_price["price"]
    print(i_goods, "-", quantity, "шт, стоимость", price, "руб")

# зачёт!
