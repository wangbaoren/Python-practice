# if...elif...else 结构:
#     if 要判断的条件1:
#         条件成立时,执行对应的操作1
#     elif 要判断的条件2:
#         条件成立时,执行对应的操作2
#     else:
#         条件不成立时,执行的操作3

# 案例1:根据用户输入的数字,判断数字是正数、负数、还是0
num = int(input("请输入数字:"))
if num == 0:
    print("该数字是0")
elif num > 0:
    print(f"{num}是正数")
else:
    print(f"{num}是负数")

# 案例2:根据输入的用户名、密码进行登录系统:admin/666888,root/547527,zhangsan/123456
username = input("请输入用户名:")
password = input("请输入密码:")
# Bool = (username == "admin" and password == "666888") or (username == "root" and password == "547527") or (username == "zhangsan" and password == "123456")
# if Bool == True:
#     print("登陆成功")
# else:
#     print("登陆失败")
if username == "admin" and password == "666888":
    print("登陆成功")
elif username == "root" and password == "547527":
    print("登陆成功")
elif username == "zhangsan" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败")

# 案例3:根据输入三角形3个边(正整数),判断是等边三角形、等腰三角形、普通三角形、还是不能构成三角形
#       构成三角形的条件:两边之和大于第三边
a = int(input("三角形第一个边:"))
b = int(input("三角形第二个边:"))
c = int(input("三角形第三个边:"))
if (a + b > c and a + c > b and b + c > a):
    if a == b == c:
        print("是等边三角形")
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print("是等腰三角形")
    else:
        print("是普通三角形")
else:
    print("不是三角形")