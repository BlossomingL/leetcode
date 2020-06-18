# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:XLin
# datetime:2020/6/19 0019 0:34
# software: PyCharm


class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        dict = {}
        n = len(envelopes)
        if n == 0:
            return 0
        # envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if envelopes[i][1] > envelopes[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        for i in range(n):
            if envelopes[i][0] not in dict:
                dict[envelopes[i][0]] = [envelopes[i][1]]
            else:
                # arr = dict[envelopes[i][0]]
                dict[envelopes[i][0]].append(envelopes[i][1])

        dict_list = sorted(dict.items(), key=lambda x: x[0])
        arr = []
        for i in range(len(dict_list)):
            arr.extend(sorted(dict_list[i][1], reverse=True))

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
