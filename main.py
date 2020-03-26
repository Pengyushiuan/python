#
# #print('Hello')
# #print('Hello world !')
# #print('Hello','world','!')
# #print('Hello \nword \n!')
# #print('Hello \n word \n !')
# #print('Good' , end = '')
# #print('Good')
#
# #x = 42
# #value = f"value of x is {x}"
# #print(x)
#
#
# flag = True #控制迴圈是否繼續執行  #15-23是全域變數
# balance = 0 #使用者餘額
# drinks = [
#     {'name': '可樂','price': 20},
#     {'name': '雪碧','price': 20},
#     {'name': '茶裏王','price': 25},
#     {'name': '原萃','price': 25},
#     {'name': '純粹喝','price': 30},
#     {'name': '水','price': 20}
# ]
#
#
# def deposit(): #()裡放要傳入的參數
#     global balance
#     value = eval(input('儲值金額:'))  # 輸入的金額建會=value
#     while value < 1:
#         print("====儲值金額需大於零====")
#         value = eval(input("儲值金額:"))
#     balance += value
#     print(f'儲值後金額為 {balance}元')
#
# def buy():
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
# while flag:
#     print('\n================')
#     select = eval(input('1. 儲值\2. 購買\n3. 查詢餘額\n4. 離開\n請選擇:'))
#
#     if select == 1: # 儲值
#         deposit()
#
#     elif select == 2: #購買
#         buy()
#     elif select == 3: #查詢餘額
#         print(f'目前餘額為 {balance}元')#代替大括號的空白
#
#     elif select == 4: #離開
#         print('bye')
#         flag = False
#         break
#
#     else: #重新輸入
#         print('====請輸入1-4之間====')
#         continue

# weight = 100
# weight1 = 80
#
# def add_weight(w1, w2):
#     result = w1 + w2
#     return result  #把裡面的值呼叫給外面的世界
#
# x = add_weight(weight, weight1)
# print(x)

# weight = 100
# weight1 = 80
#
# def add_weight(w1, w2=1):
#     result = w1 + w2
#     return result  #把裡面的值呼叫給外面的世界
#
# x = add_weight(weight)
# print(x)

# def add_weight(w1, w2=1):
#     result = w1 + w2
#     return result  #把裡面的值呼叫給外面的世界
#
# x = add_weight(weight)
# y = add_weight(weight, weight1)
# print(x, y)

# weight = 100
# weight1 = 80
#
# def add_weight(w1, w2): #這裡屬於位置賦值
#     result = w1 + w2
#     result1 = w1 / w2
#     return result, result1  #把裡面的值呼叫給外面的世界
#
# x1, x2 = add_weight(weight, weight1)
# print(x1, x2)
#
# y1, y2 = add_weight(w2=weight, w1=weight1)
# print(y1, y2)


# balance = 0 #使用者餘額
# drinks = [
#     {'name': '可樂','price': 20},
#     {'name': '雪碧','price': 20},
#     {'name': '茶裏王','price': 25},
#     {'name': '原萃','price': 25},
#     {'name': '純粹喝','price': 30},
#     {'name': '水','price': 20}
# ]
# def deposit(): #()裡放要傳入的參數
#     global balance
#     value = eval(input('儲值金額:'))  # 輸入的金額建會=value
#     while value < 1:
#         print("====儲值金額需大於零====")
#         value = eval(input("儲值金額:"))
#     balance += value
#     print(f'儲值後金額為 {balance}元')
#
# def buy():
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

import vending_machine.vending_service as machine #匯入vending_machine模組 如果不打as就需要把vending_machine全名打出來
flag = True #控制迴圈是否執行

while flag:
    print('\n================')
    select = eval(input('1. 儲值\2. 購買\n3. 查詢餘額\n4. 離開\n請選擇:'))

    if select == 1: # 儲值
        machine.deposit()

    elif select == 2: #購買
        machine.buy()
    elif select == 3: #查詢餘額
        print(f'目前餘額為 {machine.balance}元')#代替大括號的空白

    elif select == 4: #離開
        print('bye')
        flag = False
        break

    else: #重新輸入
        print('====請輸入1-4之間====')
        continue

