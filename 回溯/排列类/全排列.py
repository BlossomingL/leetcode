# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/10 0010 22:43
# software: PyCharm

class Solution:
    def permuteUnique(self, nums):
        def backtrack(nums, nums_len, path, res, visited):
            if len(path) == nums_len:
                res.append(path[:])
                return
            for i in range(nums_len):
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                        continue
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(nums, nums_len, path, res, visited)
                    visited[i] = False
                    path.pop()
        res = []
        nums_len = len(nums)
        visited = [False] * nums_len
        nums.sort()
        backtrack(nums, len(nums), [], res, visited)
        return res