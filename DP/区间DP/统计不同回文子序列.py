# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/19 0019 0:32
# software: PyCharm


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if S[i] == S[j]:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 * dp[i + 1][j - 1]
                        left = i + 1
                        right = j - 1
                        c = S[i]
                        while left < j and S[left] != c:
                            left += 1
                        while right > i and S[right] != c:
                            right -= 1
                        if left < right:
                            dp[i][j] -= dp[left + 1][right - 1]
                        elif left == right:
                            dp[i][j] += 1
                        else:
                            dp[i][j] += 2
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                # dp[i][j] = dp[i][j] + (10 ^ 9 + 7) if dp[i][j] < 0 else dp[i][j] % (10 ^ 9 + 7)
        return dp[0][n - 1] % (10 ** 9 + 7)
