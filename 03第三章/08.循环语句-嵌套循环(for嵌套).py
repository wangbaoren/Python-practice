# 根据输入的长m宽n打印一个长方形,print()自带换行效果,print("",end="\n"),end后面默认是\n也就是换行
m = int(input("长:"))
n = int(input("宽:"))
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*", end=" ")
    print()

# 嵌套案例打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i * j}", end = "\t")
    print()