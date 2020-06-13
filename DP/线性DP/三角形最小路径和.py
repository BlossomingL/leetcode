# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/14 0014 0:39
# software: PyCharm


class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp = [[float('INF')] * n for _ in range(n)]
        s = 0
        for i in range(n):
            s += triangle[i][0]
            dp[i][0] = s

        for i in range(n):
            for j in range(1, n):
                if i >= j:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])
