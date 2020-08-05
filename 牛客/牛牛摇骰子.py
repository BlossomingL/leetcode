# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/8/5 0005 10:31
# software: PyCharm

#
# 把所有询问的答案按询问顺序放入vector里
# @param arr int整型一维数组 要查询坐标的数组
# @return int整型一维数组
#


class Solution:
    def MinimumTimes(self , arr ):
        # write code here
        def bfs(end):
            queue = []
            queue.append([0, 0])
            while queue:
                val, level = queue.pop(0)
                if val == end:
                    return level
                for x in [-3, -7, -11, 3, 7, 11]:
                    queue.append([val + x, level + 1])
        res = []
        for x in range(11):
            res.append(bfs(x))
        print(res)
        out = []
        for x in arr:
            out.append(res[x % 11] + x // 11)
        return out

Solution().MinimumTimes([6,25])