def PrintFromTopToBottom(root):
    # write code here
    if not root: return []
    queue = [root]
    res = []
    while queue:
        n = len(queue)
        for _ in range(n):
            if not queue: break
            node = queue.pop(0)
            res.append(node.val)
            if node.left:             
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return []
        queue = [root]
        while len(queue):
            tmp = queue.pop(0)
            res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return res
