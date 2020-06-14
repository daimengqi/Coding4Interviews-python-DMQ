def NumberOf1Between1AndN_Solution(n):
    # write code here
    res = 0
    i = 1  # 个位开始
    while n // i != 0:
        high = n//(i*10) # 高位数
        current = (n//i) % 10  # 第i位数
        low = n - (n//i) * i  # 低位数
        if current == 0:
            res += high * i
        elif current == 1:
            res += high * i + low + 1
        else:
            res += (high+1) * i
        i *= 10
    return res

print(NumberOf1Between1AndN_Solution(20))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 一、python暴力解法
        res = ''
        for i in range(1,n+1):
            res += str(i)
        num = res.count('1')
        return num
        # 二、分析归纳法