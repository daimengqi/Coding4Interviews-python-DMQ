class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        queue = [pRoot]
        res = []
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)
        return res

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
                # 用队列，先进先出来打印；多行的实现，可以看成是王数组中加数组构成二维数组
        # 如果树为空
        if not pRoot:
            return []
        queue = [pRoot]
        result = []
        while queue:
            length = len(queue)
            row = []
            for i in queue:
                row.append(i.val)
            result.append(row)
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
                