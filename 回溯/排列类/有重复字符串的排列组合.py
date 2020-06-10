# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/10 0010 22:48
# software: PyCharm

class Solution:
    def permutation(self, S: str):
        def backtrack(S, n, step, path, res, visited):
            if step == n:
                res.append(path[:])
            for i in range(n):
                if visited[i] == 1:
                    continue
                if i > 0 and S[i] == S[i - 1] and visited[i - 1] == 0:
                    continue
                path.append(S[i])
                visited[i] = 1
                backtrack(S, n, step + 1, path, res, visited)
                path.pop()
                visited[i] = 0

        res = []
        visited = [0] * len(S)
        S = list(S)
        S.sort()
        backtrack(S, len(S), 0, [], res, visited)
        res = [''.join(s) for s in res]
        # res.sort()
        return res