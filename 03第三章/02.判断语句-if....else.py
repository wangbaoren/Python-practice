# 案例 登录功能
True_account = 1888
True_password = 6688
#1.接受用户输入的账号和密码
account = int(input("请输入账号:"))
password = int(input("请输入密码:"))
#2.判断账号和密码是否正确
if account == True_account and password == True_password:
    print("登陆成功")
else:
    print("登陆失败")

#案例:根据用户输入的年份,判断这一年是闰年还是平年
#   非整百年份,且能被4整除的年份是闰年
#   整百年份(如1900年、2000年)必须能被400整除才是闰年


year = int(input("请用户输入年份"))
# if year % 100 != 0:
#     if year % 4 == 0:
#         print("是闰年")
#     else:
#         print("是平年")
# else:
#     if year % 400 == 0:
#         print("是闰年")
#     else:
#         print("是平年")

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")