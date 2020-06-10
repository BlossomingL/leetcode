# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/10 0010 22:49
# software: PyCharm


class Solution:
    def subsets(self, nums):
        def backtrack(nums, idx, path, res):
            res.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1, path, res)
                path.pop()
        res = []
        backtrack(nums, 0, [], res)
        return res