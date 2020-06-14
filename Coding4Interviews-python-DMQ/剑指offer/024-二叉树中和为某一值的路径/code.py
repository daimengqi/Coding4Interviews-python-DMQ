### 前序遍历，深度优先遍历dfs
class Solution(object):
    def __init__(self):
        self.result_all = []
        self.array = []

    def pathSum(self, root, expectNumber):
        if not root: return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])
        self.pathSum(root.left, expectNumber)
        self.pathSum(root.right, expectNumber)
        self.array.pop()
        return self.result_all

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root:
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            # 对根节点的左右子树，继续递归，输入整数需要减去根节点的值
            # 返回二维列表
            left = self.FindPath(root.left, expectNumber - root.val)
            right = self.FindPath(root.right, expectNumber - root.val)
            for i in left+right:
                res.append([root.val] + i)
            return res
