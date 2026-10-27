# for循环本质是一种轮询遍历机制,对一批内容进行逐个处理
# for 元素 in 待处理的元素集:
#     循环体代码(对元素进行处理)
# else:
#     循环结束时,执行的代码
msg = "HELLO WORLD"
for i in msg:
    print(i)

# range语句
# 作用:生成指定规则的数字序列
# 用法一: range(end) -> 获取一个从0开始,到end结束的数字序列(不包含end本身),range(3):0,1,2
# 用法二: range(start , end) -> 获取一个从start开始,到end结束的数字序列(不包含end本身),range(4,8):4,5,6,7
# 用法三: range(start , end , step) -> 获取一个从start开始,步长为step,到end结束的数字序列(不包含end本身),range(1,10,2):1,3,5,7,9

# 案例计算1-100之间所有奇数之和
total = 0
for i in range(1,101,2):
    total += i
else:
    print(total)

# 案例计算100-500之间所有3的倍数之和
total = 0
for i in range(100,501):
    if i %3 == 0:
        total += i
else:
    print(total)