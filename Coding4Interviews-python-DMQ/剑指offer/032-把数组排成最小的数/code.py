# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        # �Զ���������򣺽�a��bתΪstr���� a��b<b+a�� ����a��ǰ��b�ں�
        # ��[a,b]Ϊ˳�����У���Ӧsorted()����Ϊ����ʽΪĬ�ϵ�false,����
        if not numbers:
            return ''
        # ����������תΪ�ַ��������뵽�ַ�������
        strnum = [str(numbers[i]) for i in range(len(numbers))]
        # �����Զ�����������ַ��������������
        strnum.sort(self.compare)
        # ƴ���ַ�����תΪ����
        return int(''.join(strnum))
    def compare(self, a, b):
        if a + b < b + a:
            return -1
        if a + b > b + a:
            return 1
        else:
            return 0 