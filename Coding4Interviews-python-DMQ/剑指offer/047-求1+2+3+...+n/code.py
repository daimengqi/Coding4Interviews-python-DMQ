def sum(n):
    try:
        1 % n
        return n + sum(n-1)
    except:
        return 0


class Solution:
    def Sum_Solution(self, n):
        return sum(n)


print(Solution().Sum_Solution(10))

# ½â·¨¶þ
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        # µÝ¹é
        if n ==1:
            return 1
        return n+self.Sum_Solution(n-1)