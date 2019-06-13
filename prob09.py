# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menu_dict = {
    '오뎅': 300,
    '순대': 400,
    '만두': 500
             }

menu = input('메뉴: ')
price = menu_dict.get(menu)
if price is None:
    price = 0

print('가격: {0}'.format(price))