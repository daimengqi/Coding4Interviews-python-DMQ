def helper(sequence):
    if len(sequence) <= 1: return True
    root = sequence[-1]
    for i in range(len(sequence)):
        if sequence[i] > root:
            break
    for j in range(i, len(sequence)-1):
        if sequence[j] < root:
            return False
    return helper(sequence[:i]) and helper(sequence[i:-1])


def VerifySquenceOfBST(sequence):
    # write code here
    if not sequence: return False
    return helper(sequence)
print(VerifySquenceOfBST([7,4,6,5]))

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # ������������������������㣬���һ��Ԫ���Ǹ��ڵ㣬ǰ��ֱ��Ǹ��ڵ������������������
        # ��������Ԫ��ֵ��С�ڸ��ڵ㣬��������Ԫ��ֵ�����ڸ��ڵ�
        length = len(sequence)
        if length == 0 :
            return False
        if length == 1:
            return True
        root = sequence[-1]
        left = 0
        # ���ڵ���������С�ڸ��ڵ�
        while sequence[left] < root:
            left += 1 
        # ���ڵ������������ڸ��ڵ�
        for i in range(left,length-1):
            if sequence[i] < root:
                return False
        # ���ҵ��ĸ��ڵ���������������еݹ��жϣ�
        return  self.VerifySquenceOfBST(sequence[: left]) or self.VerifySquenceOfBST(sequence[left: length-1])
        