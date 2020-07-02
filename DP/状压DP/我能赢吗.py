# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/30 0030 15:39
# software: PyCharm


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def dfs(a, b, cur, visited):
            if cur > b:
                return False
            if cur == b:
                return True
            for i in range(1, a + 1):
                if not visited[i]:
                    visited[i] = True
                    tmp = dfs(a, b, cur + i, visited)
                    visited[i] = False
                    if not tmp:
                        return tmp
            return False
        return dfs(maxChoosableInteger, desiredTotal, 0, [False] * (maxChoosableInteger + 1))


print(Solution().canIWin(10, 11))
