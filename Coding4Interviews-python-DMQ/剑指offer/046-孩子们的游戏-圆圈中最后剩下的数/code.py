class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        n = list(range(n))
        if not n: return -1
        i = 0
        while len(n) != 1:
            for _ in range(m-1):
                i += 1
                i %= len(n)
            n.pop(i)
        return n

print(Solution().LastRemaining_Solution(5, 3))

#解法二
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # 一、约瑟夫环
        if not m or not n:
            return -1
        start = 0
        end = -1
        nums = list(range(n))
        
        while n:
            k = (start+m-1) % n
            end = nums.pop(k)
            start = k
            n -= 1
        return end