# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ��¼������������ƽ�����������ֹ�ôεݹ�
    res = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # ƽ�����������ڵ�������ĸ߶ȲС�ڵ���1
        # �����ظ�ÿ���ڵ㶼ȥ��һ�θ߶�
        self.find_depth(pRoot)
        return self.res
    
    # �����нڵ�����
    def find_depth(self, root):
        if not root:
            return 0
        left = self.find_depth(root.left) + 1
        right = self.find_depth(root.right) + 1
        # ������ƽ�����ж�
        if abs(left - right) > 1:
            self.res = False
        return max(left, right)
