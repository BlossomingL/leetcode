# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/13 0013 23:51
# software: PyCharm

class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # dp[i]表示到第i个为止最长上升子序列的长度
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
