# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 记录若有子树不是平衡二叉树，终止该次递归
    res = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # 平衡二叉树任意节点的子树的高度差都小于等于1
        # 避免重复每个节点都去求一次高度
        self.find_depth(pRoot)
        return self.res
    
    # 求树中节点的深度
    def find_depth(self, root):
        if not root:
            return 0
        left = self.find_depth(root.left) + 1
        right = self.find_depth(root.right) + 1
        # 二叉树平衡性判断
        if abs(left - right) > 1:
            self.res = False
        return max(left, right)
