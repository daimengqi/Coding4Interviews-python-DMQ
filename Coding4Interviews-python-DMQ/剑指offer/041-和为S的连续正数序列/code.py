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

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # C++˫ָ�뼼��������ָ��ȷ�����ڵ�λ�úʹ�С
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
        
