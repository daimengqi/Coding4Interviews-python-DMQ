
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        queue = [pRoot]
        j = -1
        while queue:
            j += 1
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if j % 2:
                temp.reverse()
            res.append(temp)
        return res

# �ⷨ��
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        # �ö���˳��洢����ÿ���㣬��result����洢���нڵ���ֵ��ʵ�ְ��д�ӡ
        if not pRoot:
            return []
        result = []
        queue = [pRoot]
        level = 1
        while queue:
            nodeList = []
            row = []
            for item in queue:
                if item.left:
                    nodeList.append(item.left)
                if item.right:
                    nodeList.append(item.right)
                row.append(item.val)
            queue = nodeList
            if level % 2 == 0:
                row.reverse()
            if len(row) > 0:
                result.append(row)
            level += 1
        return result