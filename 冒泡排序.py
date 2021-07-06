# _*_ coding: utf-8/GBK/gb18030 _*_
#@Time    :2021/7/6 10:06

import random
import time
nums = []
for i in range(0, 1000):
    num = random.randint(0, 10000)
    nums.append(num)
start = time.time()
n = len(nums)
for i in range(n-1):
    for j in range(n-i-1):
        if nums[j] > nums[j+1]:
            nums1 = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = nums1
print(nums)
end = time.time()
print(end-start)