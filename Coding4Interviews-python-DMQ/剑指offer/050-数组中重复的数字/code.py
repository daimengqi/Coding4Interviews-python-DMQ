class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        map = [0] * 1000
        for n in numbers:
            if map[n] == 1:
                duplication[0] = n
                return True
            else:
                map[n] = 1
        return False

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        s = []
        for i in numbers:
            if i in s:
                duplication[0] = i
                return True
            else:
                s.append(i)
        return False