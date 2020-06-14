class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array: return []
        lp = 0
        rp = len(array) - 1
        res = [array[-1]] * 2
        while lp < rp:
            tmp = array[lp] + array[rp]
            if tmp > tsum:
                rp -= 1
            elif tmp < tsum:
                lp += 1
            else:
                if array[lp] * array[rp] < res[0] * res[1]:
                    res[0], res[1] = array[lp], array[rp]
                lp += 1
                rp -= 1

        return res if res[0] + res[1] == tsum else []

print(Solution().FindNumbersWithSum([], 0))

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # ��ͷ��ʼ��ƥ�䣬��Ϊ�ǵ������飬�˻���С�ض�Ϊ�����ҵ��ģ���7+8=15 1+14=15�˻�1*14С
        # ����ֱ�Ӵ�array��һ����ʼ�������ң��ҵ��ĵ�һ�����������ľ��ǳ˻���С
        for i in array:
            if tsum-i in array:
                if tsum-i == i:
                    if array.count(i) > 1:
                        return [i, i]
                else:
                    return [i , tsum-i]
        return []