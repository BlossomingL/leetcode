# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/10 0010 22:40
# software: PyCharm

class Solution:
    def subsets(self, nums):
        res = []

        def dfs(nums, res, path, start, nums_len):
            res.append(path[:])
            for i in range(start, nums_len):
                path.append(nums[i])
                dfs(nums, res, path, i + 1, nums_len)
                path.pop()

        dfs(nums, res, [], 0, len(nums))
        return res