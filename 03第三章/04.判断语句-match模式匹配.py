# 结构模式匹配就是用一个清晰的模板去精准的匹配数据的结构和内容,匹配成功则执行响应的操作
day = input("请输入星期:")
match day:
    case "1":
        print("星期一")
    case "2":
        print("星期二")
    case "3":
        print("星期三")
    case "4":
        print("星期四")
    case "5":
        print("星期五")
    case "6":
        print("星期六")
    case "7":
        print("星期日")
    case _:
        print("输入错误")


# 案例:简易计算器
num1 = int(input("请输入第一个数字"))
num2 = int(input("请输入第二个数字"))
oper = input("请输入运算符")
match oper:
    case "+":
        print(f"结果是{num1+num2}")
    case "-":
        print(f"结果是{num1-num2}")
    case "*":
        print(f"结果是{num1*num2}")
    case "/":
        print(f"结果是{num1/num2}")
    case "//":
        print(f"结果是{num1//num2}")
    case "%":
        print(f"结果是{num1%num2}")
    case "**":
        print(f"结果是{num1**num2}")
    case _:
        print("输入的运算符无效")
