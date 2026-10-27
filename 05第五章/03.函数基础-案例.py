def triangle_area(l , h):
    """
    根据传入的三角形的底和高,计算三角形的面积
    :param l: 三角形的底
    :param h: 三角形的高
    :return: 三角形的面积
    """
    area = (l * h) / 2
    return area
print("三角形的面积",triangle_area(3,4))

def count_aeiou(s):
    """
    计算字符串中的元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for i in s:
        if i in "aeiouAEIOU":
            num += 1
    return num
print("字符串中元音字母个数",count_aeiou("Hello,World!"))

#max()计算最大值,min()计算最小值,sum()求和,len()计算长度
def class_score(score_list):
    """
    计算传入的班级学员高考成绩列表中的最高分,最低分,平均分
    :param score_list: 班级学院成绩
    :return: 最高分,最低分,平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list))
    return max_s, min_s, avg_s
print(class_score([1,2,3,4,5]))

