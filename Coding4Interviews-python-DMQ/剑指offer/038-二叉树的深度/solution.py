class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        queue = [pRoot]
        deep = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            deep += 1
        return deep

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # 一、递归：
        # 二叉树只有根节点深度为1，递归法，二叉树深度为左右子树深度的最大值+1
        if not pRoot:
            return 0
        depth = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        return depth
    
        # 二、层次遍历，用队列完成
                