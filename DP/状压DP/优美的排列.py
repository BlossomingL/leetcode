# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/7/2 0002 10:14
# software: PyCharm


class Solution:
    def __init__(self):
        self.res = 0

    def countArrangement(self, N: int) -> int:

        # 回溯
        def backtrack(N, step, visited):
            if step == N + 1:
                self.res += 1
                return
            for i in range(1, N + 1):
                if not visited[i]:
                    if i % step == 0 or step % i == 0:
                        visited[i] = True
                        backtrack(N, step + 1, visited)
                        visited[i] = False
        backtrack(N, 1, [False for _ in range(N + 1)])
        return self.res
