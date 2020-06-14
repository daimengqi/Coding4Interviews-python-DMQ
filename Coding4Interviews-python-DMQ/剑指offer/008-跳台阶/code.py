class Solution(object):
    def numWays(self, n):
        if n == 0: return 1
        f1 = 1
        f2 = 2
        if n == 1: return f1
        if n == 2: return f2
        for _ in range(n-2):
            f2, f1 = f1+f2, f2
        return f2 % 1000000007

# 解法二
class Solution:
    def jumpFloor(self, number):
        # write code here
        # a.假定第一次跳的是一阶，那么剩下的n-1个台阶共有跳法f(n-1);
        # b.假定第一次跳的是2阶，那么剩下的是n-2个台阶共有跳法f(n-2)
        # c.总跳法为: f(n) = f(n-1) + f(n-2) 
        # d.然后通过实际的情况可以得出：只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
        # e.所以跳台阶法是斐波那契数列，属于递归
        res = [1,1,2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]
