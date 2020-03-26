# balance = 0 #使用者餘額
#
# # 品項
# drinks = [
#     {'name': '可樂','price': 20},
#     {'name': '雪碧','price': 20},
#     {'name': '茶裏王','price': 25},
#     {'name': '原萃','price': 25},
#     {'name': '純粹喝','price': 30},
#     {'name': '水','price': 20}
# ]
# def add(x, y):
#     """
#     數字相加
#     :param x:數字1
#     :param y:數字2
#     :return:相加結果
#     """
#     return x + y
# def deposit(): #()裡放要傳入的參數
#     """
#     儲值功能
#     :return: nothing #沒有傳入甚麼
#     """
#     global balance
#     value = eval(input('儲值金額:'))  # 輸入的金額建會=value
#     while value < 1:
#         print("====儲值金額需大於零====")
#         value = eval(input("儲值金額:"))
#     balance += value
#     print(f'儲值後金額為 {balance}元')
#
# def buy():
# # 購買功能
#     global balance, drinks
#     print('請選擇商品')
#     for i in range(len(drinks)):
#         print(f'{i + 1}. {drinks[i]["name"]} {drinks[i]["price"]}元')  # i+1是因為程式從0開始
#
#     choose = eval(input('請選擇編號:'))
#     while choose < 1 or choose > 6:
#         print("請輸入1-6之間")
#         choose = eval(input('請選擇:'))
#
#     buy_drink = drinks[choose - 1]  # -1是因為從0開始,index都是從0,1,2,3...
#     while balance < buy_drink['price']:
#         print('=====餘額不足，需要儲值嗎?====')
#         want_deposit = input('y/n?')
#         if want_deposit == 'y':
#             deposit()
#         elif want_deposit == 'n':
#             break
#         else:
#             print('====請重新輸入====')
#
#     #儲值後餘額大於商品金額再購買
#     if balance < buy_drink['price']:
#         print('====餘額不足====')
#         deposit()
#     else:
#         balance -= buy_drink['price']
#         print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
#         print(f'購買後餘額為 {balance}元')

# from vending_machine.data import Drink
# balance = 0 #使用者餘額
#
# # 品項
# drinks = [
#     Drink('可樂',  20),
#     Drink('雪碧', 20),
#     Drink('茶裏王', 25),
#     Drink('原萃', 25),
#     Drink('純粹喝', 30),
#     Drink('水', 20),
#     # {'name': '可樂', 'price': 20},
#     # {'name': '雪碧', 'price': 20},
#     # {'name': '茶裏王', 'price': 25},
#     # {'name': '原萃', 'price': 25},
#     # {'name': '純粹喝', 'price': 30},
#     # {'name': '水', 'price': 20}
# ]
# def add(x, y):
#     """
#     數字相加
#     :param x:數字1
#     :param y:數字2
#     :return:相加結果
#     """
#     return x + y
# def deposit(): #()裡放要傳入的參數
#     """
#     儲值功能
#     :return: nothing #沒有傳入甚麼
#     """
#     global balance
#     value = eval(input('儲值金額:'))  # 輸入的金額建會=value
#     while value < 1:
#         print("====儲值金額需大於零====")
#         value = eval(input("儲值金額:"))
#     balance += value
#     print(f'儲值後金額為 {balance}元')
#
# def buy():
# # 購買功能
#     global balance, drinks
#     print('請選擇商品')
#     for i in range(len(drinks)):
#         print(f'{i + 1}. {drinks[i].name} {drinks[i].price}元')  # i+1是因為程式從0開始
#
#     choose = eval(input('請選擇編號:'))
#     while choose < 1 or choose > 6:
#         print("請輸入1-6之間")
#         choose = eval(input('請選擇:'))
#
#     buy_drink = drinks[choose - 1]  # -1是因為從0開始,index都是從0,1,2,3...
#     while balance < buy_drink.price:
#         print('=====餘額不足，需要儲值嗎?====')
#         want_deposit = input('y/n?')
#         if want_deposit == 'y':
#             deposit()
#         elif want_deposit == 'n':
#             break
#         else:
#             print('====請重新輸入====')
#
#     #儲值後餘額大於商品金額再購買
#     if balance < buy_drink.price:
#         print('====餘額不足====')
#         deposit()
#     else:
#         balance -= buy_drink['price']
#         print(f'已購買{buy_drink.name} {buy_drink.price}元')
#         print(f'購買後餘額為 {balance}元')

