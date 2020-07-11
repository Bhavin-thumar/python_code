# def leap_year(year):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         return True
#     # if year % 4 == 0 and year % 100 != 0:
#     #     return True
#     else:
#         return False
#
#
# year = 0
# while year < 1900 or year > 100000:
#     year = int(input("Enter year between 1900 and 100000 :"))
#
# print(leap_year(year))

#
# def withdraw_list(current_balance):
#     div_list = []
#     for i in range(current_balance):
#         if i == 0:
#             i = 1
#         if current_balance % i == 0:
#             div_list.append(i)
#     return div_list
#
#
# current_balance = 18
# withdraw = []
# max_withdraw = 0
# days = 0
#
# while current_balance > 0:
#     withdraw = withdraw_list(current_balance)
#     max_withdraw = withdraw[len(withdraw)-1]
#     print("\nCurrent Balance :", current_balance)
#     print("Withraw Amount :", max_withdraw)
#     current_balance -= max_withdraw
#     print("Remaining Amount :", current_balance)
#     days += 1
#
# print(withdraw_list(current_balance))
# print("Total days", days)

orders = "10 11 12 2 100"   #input("Enter the orders :")
order_list = list(map(lambda x: int(x), orders.split()))
print(order_list)
# orders_num = []
#
# combined = ""
# for i in range(len(orders)+1):
#     if i == len(orders):
#         orders_num.append(int(combined))
#         combined = ""
#         break
#     if orders[i].isdigit():
#         combined += orders[i]
#     else:
#         orders_num.append(int(combined))
#         combined = ""
#
# print(orders_num)