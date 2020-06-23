# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/23 0023 18:37
# software: PyCharm


class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        new_nums = [1] * (n + 2)
        for i in range(n):
            new_nums[i + 1] = nums[i]
        print(new_nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + new_nums[i] * new_nums[k] * new_nums[j])

        return dp[0][n + 1]

