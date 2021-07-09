# _*_ coding: utf-8/GBK/gb18030 _*_
#@Time    :2021/7/8 8:48

import random
import time

nums = []
for i in range(0, 1000):
    num = random.randint(0, 1000000)
    nums.append(num)

def insort(nu):
    # 从1开始计数
    for i in range(1, len(nu)):
        # 第一个数赋值va
        va = nu[i]
        p = i
        # 循环索引大于0 还要前一个数大于第一个数
        while p > 0 and nu[p-1] > va:
            # 前第一个数赋值给第一个数
            nu[p] = nu[p-1]
            # po减一
            p -= 1
        # 第一个数赋值给倒数第一个数
        nu[p] = va
    # 返回 nu
    return nu


start = time.time()
insort(nums)
# for i in range(1, len(nums)):
#     # 根据依次循环的索引的值,赋值给va
#     va = nums[i]
#     # 索引赋值给po
#     p = i
#     # 修改成 < 为倒序
#     while p > 0 and nums[p - 1] > va:
#         # 前一个数赋值给第一个数
#         nums[p] = nums[p - 1]
#         # po减一
#         p -= 1
#         nums[p] = va
#
# print(nums)
end = time.time()
print(end-start)
