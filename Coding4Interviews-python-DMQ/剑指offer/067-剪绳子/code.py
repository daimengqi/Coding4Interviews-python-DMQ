# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        # һ��̰���㷨
        # ���Ⱦ���֤������n>=4 ��ʱ�򣬷ֳ������ֵ��m���У�ÿ������ֻ������2����3����
        # ��2�ĸ����϶�С��3������Ϊ2*2*2<3*3
        # ��˿�����Ҫ���ֳɵ�3�ĸ��������ճ���3ȡ��
        if number == 2:
            return 1
        elif number == 3:
            return 2
        else:
            x = number % 3
            if x == 0:
                return pow(3, number//3)
            if x == 1:
                return 2*2*pow(3, number//3 - 1)
            else:
                return 2*pow(3, number//3)
                