class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        stack.reverse()
        return ' '.join(stack)

print(Solution().ReverseSentence("I am a student."))

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        # һ��python�����ⷨ
        # return ' '.join(s.split(' ')[: : -1])
        # ��
        s1 = s.split(' ')
        s1.reverse()
        return ' '.join(s1)