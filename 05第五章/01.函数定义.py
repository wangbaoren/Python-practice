"""
函数定义与调用:
    #定义函数
    def 函数名(参数列表)
        函数体
        ...
        return 返回值
    #调用函数
    函数名(参数)
"""

#计算圆的面积,多个返回值会封装到元组之中;round(值/表达式,
# 需要保留几位小数),用help()函数可以查看函数的说明文档
def circle_area(r):
    """
    该函数用于根据圆的半径,计算圆的面积和周长
    :param r: 圆的半径
    :return: 圆的面积,圆的周长
    """
    area = 3.14 * r * r
    return area, round(2 * 3.14 * r , 1) , 2 * 3.14 * r
help(circle_area)
c_area = circle_area(10)
print(c_area)
print(circle_area(10))
#解包
area , len , l = circle_area(10)
print(area)
print(len)

#计算长方形面积
def rectangle_area(l, w):
    """
    根据长方形的长和宽计算长方形的面积
    :param l: 长方形的长
    :param w: 长方形的宽
    :return: 长方形的面积
    """
    area = l * w
    return area
r_area = rectangle_area(10, 20)
print(rectangle_area(10, 20))