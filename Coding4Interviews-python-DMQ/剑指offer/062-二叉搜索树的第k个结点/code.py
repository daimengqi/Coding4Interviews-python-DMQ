
class Solution:
    # 返回对应节点TreeNode
    
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot: return None
        stack = []
        while pRoot or stack:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop()
            k -= 1
            if k == 0:
                return pRoot
            pRoot = pRoot.right

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 该二叉搜索树中序遍历2345678，正好是从小到大顺序序列
        # 树的问题就是递归
        global result
        result = []
        self.midTraversal(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k-1]
        
    # 定义中序遍历函数
    def midTraversal(self, root):
        if not root:
            return None
        self.midTraversal(root.left)
        result.append(root)
        self.midTraversal(root.right)