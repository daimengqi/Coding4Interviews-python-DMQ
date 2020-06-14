class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        stack.reverse()
        return ' '.join(stack)

print(Solution().ReverseSentence("I am a student."))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        # 一、python暴力解法
        # return ' '.join(s.split(' ')[: : -1])
        # 二
        s1 = s.split(' ')
        s1.reverse()
        return ' '.join(s1)