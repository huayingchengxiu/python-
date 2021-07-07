# _*_ coding: utf-8/GBK/gb18030 _*_
#@Time    :2021/7/4 15:52

import random
import time

nums = []
# 1.循环100次
for i in range(0, 10000):
    # 2.生成随机数的范围
    num = random.randint(0, 100000)
    # 3.添加到列表中
    nums.append(num)

# 用def XX():的方式创建函数,括号内是参数可以写也可以不写
# 这里ary是一个传入参数,rse是一个自定义参数,可传可不传.
def qck_sort(ary):
    if len(ary) > 0:
        # 这里确定用列表的第一个值作为关键值
        pot = ary[0]
        # 循环列表,用每一个数和绝对值比较,下面是小于的关键值的
        les = [x for x in ary if x < pot]
        gtr = [x for x in ary if x > pot]
        # 正序
        return qck_sort(les) + [pot] + qck_sort(gtr)

        #  倒序 return qck_sort(gtr) + [pot] + qck_sort(les)
    return []


start = time.time()
print(qck_sort(nums))
end = time.time()
print(end-start)