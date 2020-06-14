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

# �ⷨ��
class Solution:
    def jumpFloor(self, number):
        # write code here
        # a.�ٶ���һ��������һ�ף���ôʣ�µ�n-1��̨�׹�������f(n-1);
        # b.�ٶ���һ��������2�ף���ôʣ�µ���n-2��̨�׹�������f(n-2)
        # c.������Ϊ: f(n) = f(n-1) + f(n-2) 
        # d.Ȼ��ͨ��ʵ�ʵ�������Եó���ֻ��һ�׵�ʱ�� f(1) = 1 ,ֻ�����׵�ʱ������� f(2) = 2
        # e.������̨�׷���쳲��������У����ڵݹ�
        res = [1,1,2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]
