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

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # 二叉搜索树后序遍历序列满足，最后一个元素是根节点，前面分别是根节点的左子树和右子树。
        # 左子树的元素值都小于根节点，右子树的元素值都大于根节点
        length = len(sequence)
        if length == 0 :
            return False
        if length == 1:
            return True
        root = sequence[-1]
        left = 0
        # 根节点左子树都小于根节点
        while sequence[left] < root:
            left += 1 
        # 根节点右子树都大于根节点
        for i in range(left,length-1):
            if sequence[i] < root:
                return False
        # 对找到的根节点的左右子树，进行递归判断：
        return  self.VerifySquenceOfBST(sequence[: left]) or self.VerifySquenceOfBST(sequence[left: length-1])
        