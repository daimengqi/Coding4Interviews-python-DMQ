class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0
        flag = 1
        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                continue
            elif i == 0 and s[i] == '-':
                flag = -1
                continue
            n = ord(s[i]) - ord('0')
            if n>=0 and n<=9:
                res = 10 * res + n
            else:
                return False
        return res * flag

print(Solution().StrToInt('-1234'))

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        # һ��python�����ⷨ
        # try:
            # return int(s)
        # except Exception as e:
            # return 0
        # ����
        numList = ['0','1','2','3','4','5','6','7','8','9'] # �Ϸ��ַ�����
        label = 1 # ���������
        sum = 0
        if s == '':
            return 0
        if s[0] == '+':
            label = 1
            s = s[1:]
        elif s[0] =='-':
            label = -1
            s = s[1:]
        for char in s:
            if char in numList: # ����ַ����ǺϷ���
                sum = sum * 10 + numList.index(char)
            elif char not in numList: # ����ַ����ǷǷ���
                sum = 0
                break
        return sum * label