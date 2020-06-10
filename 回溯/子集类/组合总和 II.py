# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/10 0010 22:47
# software: PyCharm

class Solution:
    def func(self, candidates, target, arr, res, start, end):
        if target == 0:
            res.append(arr[:])

        for i in range(start, end):
            residual = target - candidates[i]
            if residual < 0:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            arr.append(candidates[i])
            self.func(candidates, residual, arr, res, i + 1, end)
            arr.pop()

    def combinationSum2(self, candidates, target: int):
        arr = []
        res = []
        temp = []
        candidates.sort()
        self.func(candidates, target, arr, res, 0, len(candidates))
        return res