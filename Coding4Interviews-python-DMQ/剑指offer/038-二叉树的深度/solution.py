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

# �ⷨ��
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # һ���ݹ飺
        # ������ֻ�и��ڵ����Ϊ1���ݹ鷨�����������Ϊ����������ȵ����ֵ+1
        if not pRoot:
            return 0
        depth = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        return depth
    
        # ������α������ö������
                