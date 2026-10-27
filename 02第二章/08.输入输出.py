# input语句(函数)的功能是获取键盘输入的数据,用法为 s = input(提示信息),无论键盘输入的是什么类型的数据,得到的数据永远都是字符串类型
# print语句(函数)的功能是将数据输出到控制台,用法为 print(数据)
name = input("请输入您的姓名:")
print(f"欢迎光临{name}先生")
age = input("xxxx")
print(f"{int(age)+5}")

# 案例练习:银行卡有10000元,输入密码,取钱,显示余额
total = 10000
password = input("请输入密码:")
print(f"输入正确,您的密码是{password}")
num = input("输入您要取款的金额:")
print(f"您的余额为{total-int(num)}")
