# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/10 0010 22:51
# software: PyCharm

class Solution:
    def letterCasePermutation(self, S: str):
        # f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        # return map("".join, itertools.product(*map(f, S)))

        def permutation(nums, idx, path, res):
            res.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])  # 横向
                permutation(nums, i + 1, path, res)  # 纵向
                path.pop()

        n = len(S)
        arr = []
        S = S.lower()
        for i in range(n):
            s = S[i]
            if 'a' <= s <= 'z':
                arr.append(i)

        res = []
        permutation(arr, 0, [], res)

        # print(res)
        out = []
        for x in res:
            tmp = list(S)
            for y in x:
                tmp[y] = chr(ord(tmp[y]) - ord('a') + ord('A'))
            out.append(''.join(tmp))
        return out

