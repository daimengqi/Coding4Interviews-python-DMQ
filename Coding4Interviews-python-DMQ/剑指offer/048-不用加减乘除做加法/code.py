from ctypes import *

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = c_int(num1 ^ num2).value  # 不带进位的相加结果
            num2 = c_int((num1 & num2) << 1).value  # 带进位
            num1 = temp
        return num1

print(Solution().Add(-1, 23))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        # 一、python暴力解法：
        # arr = []
        # arr.append(num1)
        # arr.append(num2)
        # return sum(arr)

        # 二、位运算：
        # 两个数异或：相当于每一位相加，而不考虑进位；两个数相与，并左移一位：相当于求得进位；将上述两步的结果相加；
        # 注意python没有无符号右移操作，所以需要越界检查
        # 按位与运算：相同位的两个数字都为1，则为1；若有一个不为1，则为0。
        # 按位异或运算：相同位不同则为1，相同则为0。
        if not num1:
            return num2
        while num2!=0:
            res=num1^num2
            carray=(num1&num2)<<1
            num1=res & 0xFFFFFFFF
            num2=carray
        return num1 if num1 >> 31 == 0 else num1 - 4294967296

