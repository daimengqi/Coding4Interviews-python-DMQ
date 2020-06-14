# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 思路：按顺序把每个丑数放在数组中，求下一个丑数。下一个丑数必定由有数组中的某一个丑数A * 2， B * 3， C * 5 的中的最小值得来。
        if index < 1:
            return 0
        # 加入第一个丑数
        res = [1]
        # 三个下标用于记录丑数的位置
        t2 = t3 = t5 = 0
        next = 1
        while next < index:
            # 三个数都可能是丑数，取其中最小值加入数组
            min_num = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(min_num)
            if res[t2]*2 <= min_num:
                t2 += 1
            if res[t3]*3 <= min_num:
                t3 += 1
            if res[t5]*5 <= min_num:
                t5 += 1
            next += 1
        return  res[index - 1]