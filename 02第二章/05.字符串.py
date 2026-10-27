# 字符串有三种定义方式
# 双引号定义
s1 = "Hello"
# 单引号定义
s2 = 'Python'
#三引号定义(多行字符串)
s3 = """
    尊敬的用户:
        xxxxxxxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxxxxxx
        xxx
"""
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

# 转义字符
# \' 单引号  \" 双引号  \n 换行符  \t 制表符:增加缩进,缩进一个制表符(tab)的大小
msg = 'It\'s very easy!'
print(msg)
print("xxxxxxxxxxxxx!ttttttttttttt")
print("xxxxxxxxxxxxx!\nttttttttttttt")
print("xx\txxxxxxxxxxx!\n\tttttttttttttt")