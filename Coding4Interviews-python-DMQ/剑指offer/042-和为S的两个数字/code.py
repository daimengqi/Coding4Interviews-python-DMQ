class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array: return []
        lp = 0
        rp = len(array) - 1
        res = [array[-1]] * 2
        while lp < rp:
            tmp = array[lp] + array[rp]
            if tmp > tsum:
                rp -= 1
            elif tmp < tsum:
                lp += 1
            else:
                if array[lp] * array[rp] < res[0] * res[1]:
                    res[0], res[1] = array[lp], array[rp]
                lp += 1
                rp -= 1

        return res if res[0] + res[1] == tsum else []

print(Solution().FindNumbersWithSum([], 0))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 两头开始找匹配，因为是递增数组，乘积最小必定为最先找到的，如7+8=15 1+14=15乘积1*14小
        # 所以直接从array第一个开始遍历查找，找到的第一个符合条件的就是乘积最小
        for i in array:
            if tsum-i in array:
                if tsum-i == i:
                    if array.count(i) > 1:
                        return [i, i]
                else:
                    return [i , tsum-i]
        return []