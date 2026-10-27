# 逻辑运算符:
# 逻辑与(并且): and 同时成立才是符合条件(左右两边都为True,结果才为True)
# 逻辑或(或者): or 一边成立就符合条件(只要左右两边为True,结果就为True)
# 逻辑非(取反): not 取反操作,True变为False,False变为True

#键盘输入一个数判断数字是否在10-20之间
num1 = int(input("输入一个数字:"))
print(f"{num1}是否在10-20之间,{num1 >= 10 and num1 <= 20}")

#键盘输入一个数判断数字是否不在10-20之间
num1 = int(input("输入一个数字:"))
print(f"{num1}是否不在10-20之间,{num1 < 10 or num1 > 20}")