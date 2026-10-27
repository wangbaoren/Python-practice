# while循环语句结构:
#     while 条件表达式:
#         循环体语句1
#         循环体语句2
#         ...
#     else:(可有可无)
#         条件为False,循环正常结束时执行
i = 0
while i < 10:
    print("人生苦短,我要学python")
    i += 1
else:
    print("循环结束")

# 案例:1-100所有偶数之和
total = 0
num = 1
while num <= 100:
    if(num % 2 == 0):
        total += num
    num += 1
else:
    print(f"1-100所有偶数之和是{total}")