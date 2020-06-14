class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: return 0
        numbers.sort()
        cnt = 0
        jokers = 0
        pre = None
        for i in range(len(numbers)):
            if numbers[i] == 0:
                jokers += 1
            else:
                if pre is None:
                    pre = numbers[i]
                else:
                    if pre == numbers[i]: return 0
                    cnt += numbers[i] - pre - 1
                    pre = numbers[i]
        cnt -= jokers
        return cnt <= 0

print(Solution().IsContinuous([0,3,1,6,4]))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        # 一：max-min<5;除0外没有重复数字；数组长度为5
        if not numbers:
            return False
        if numbers == [0,0,0,0,0]:
            return False
        kings = []
        others = []
        numbers.sort()
        for i in range(5):
            if numbers[i] == 0:
                kings.append(numbers[i])
            else:
                others.append(numbers[i])
        if (max(others) - min(others)) < 5 and len(others) == len(set(others)):
            return True
        else:
            return False