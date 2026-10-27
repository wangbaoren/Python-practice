"""
案例:根据输入的用户名和密码执行登陆操作
1.正确的用户名和密码为 admin/666888,123456/777888,111/111222
2.输入用户名和密码进行登录,直到登录成功;如果登陆失败,继续输入用户名和密码
3.输入的用户名和密码不能为空
4.登录成功:输出"登陆成功"
5.登陆失败:输出"用户名或密码错误"

关键字:
    break:只能出现在循环中,表示结束,跳出循环的含义
    continue:只能够出现在循环中,中断当前循环,直接进入下次循环
"""
while True:
    # 1.录入用户名和密码:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "" or password == "":
        print("用户名或密码不能为空")
        continue#结束当前循环,直接进入下一轮循环
    if username == "admin" and password == "666888":
        print("登陆成功")
        break
    elif username == "123456" and password == "777888":
        print("登陆成功")
        break
    elif username == "111" and password == "111222":
        print("登陆成功")
        break
    else:
        print("登陆失败")