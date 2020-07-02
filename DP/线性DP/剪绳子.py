# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/30 0030 20:36
# software: PyCharm

class Solution:
    def CutRope(self , N ):
        # write code here
        dp = [i for i in range(N + 1)]
        for i in range(2, N + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j))
        print(dp)
        return dp[-1]

print(Solution().CutRope(8))