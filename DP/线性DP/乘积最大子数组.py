# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/14 0014 22:55
# software: PyCharm

class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)

        # 自己写
        # dp_min = nums[:]
        # dp_max = nums[:]
        # for i in range(1, n):
        #     # 乘或者不乘以当前数
        #     if nums[i] < 0:
        #         dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
        #         dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])
        #     else:
        #         dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
        #         dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])
        # return max(dp_max)

        # 优化，不需要两个数组，可以直接用两个变量存储当前连乘最大最小值
        multi_min = multi_max = nums[0]
        res = multi_max
        for i in range(1, n):
            a = max(multi_min * nums[i], multi_max * nums[i], nums[i])
            res = max(a, res)
            b = min(multi_max * nums[i], multi_min * nums[i], nums[i])
            multi_max, multi_min = a, b
        return res