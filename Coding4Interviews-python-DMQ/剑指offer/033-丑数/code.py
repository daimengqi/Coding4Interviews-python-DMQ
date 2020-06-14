# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # ˼·����˳���ÿ���������������У�����һ����������һ�������ض����������е�ĳһ������A * 2�� B * 3�� C * 5 ���е���Сֵ������
        if index < 1:
            return 0
        # �����һ������
        res = [1]
        # �����±����ڼ�¼������λ��
        t2 = t3 = t5 = 0
        next = 1
        while next < index:
            # �������������ǳ�����ȡ������Сֵ��������
            min_num = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(min_num)
            if res[t2]*2 <= min_num:
                t2 += 1
            if res[t3]*3 <= min_num:
                t3 += 1
            if res[t5]*5 <= min_num:
                t5 += 1
            next += 1
        return  res[index - 1]