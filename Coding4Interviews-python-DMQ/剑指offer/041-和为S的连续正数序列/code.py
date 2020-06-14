class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        windows = []
        sum = 0
        for t in range(1, tsum):
            windows.append(t)
            sum += t
            while sum > tsum:
                sum -= windows.pop(0)
            if sum == tsum:
                res.append(windows[:])

        return res    

print(Solution().FindContinuousSequence(100))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # C++双指针技术，左右指针确定窗口的位置和大小
        if tsum < 3:
            return []
        res = []
        for i in range(1, tsum):
            current = 0 
            j = i
            while current < tsum:
                current += j 
                j += 1
            if current == tsum:
                res.append(range(i, j))
        return res
        
