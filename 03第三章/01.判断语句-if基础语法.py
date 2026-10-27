# if 要判断的条件:
#     条件成立时,要执行对应的操作
score = 700
if score > 650:
    print("xxxxxxx")

# 案例 登录功能
True_account = 1888
True_password = 6688
#1.接受用户输入的账号和密码
account = int(input("请输入账号:"))
password = int(input("请输入密码:"))
#2.判断账号和密码是否正确
Bool = account == True_account and password == True_password
print(Bool)
if Bool == True:
    print("登陆成功")
# 3.登陆失败提示
if Bool == False:
    print("登陆失败")

# 另一种
# if account == True_account and password == True_password:
#     print("登陆成功")
# if account != True_account or password != True_password:
#     print("登陆失败")
