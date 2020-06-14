class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        map = {}
        res = []
        for n in array:
            map[n] = map.get(n, 0) + 1
        for n in array:
            if map[n] == 1:
                res.append(n)
        return res

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        tmp = []
        for i in array:
            if i in tmp:
                tmp.remove(i)
            else:
                tmp.append(i)
        return tmp



