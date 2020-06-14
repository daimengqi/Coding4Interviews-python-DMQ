class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(treeA, treeB):
    if not treeB:
        return True
    elif not treeA:
        return False
    elif treeA.val != treeB.val:
        return False
    else:
        return helper(treeA.left, treeB.left) and helper(treeA.right, treeB.right)


def HasSubtree(pRoot1, pRoot2):
    # write code here
    if not pRoot1 or not pRoot2: return False
    # 2 是不是 1的子树
    res = False
    if pRoot1.val == pRoot2.val:
        res = helper(pRoot1, pRoot2)
    if res: 
        return True
    else:
        return HasSubtree(pRoot1.left, pRoot2) or HasSubtree(pRoot1.right, pRoot2)
        
# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 第一步，设定函数递归判断树A和树B是否具有相同的结构。（两树的根节点、左右子树都相同）
        # 第二步，遍历，查看B与A，或者B与A的左子树，或者B与A的右子树是否相同。满足一个即为子结构

        if pRoot1 == None or pRoot2 == None:
            return False
        else:
            return self.is_subTree(pRoot1, pRoot2) or self.is_subTree(pRoot1.left, pRoot2) or self.is_subTree(pRoot1.right, pRoot2)
    
    # 递归遍历判断树的每个节点是否相同
    def is_subTree(self, a, b):
        # 如果B树遍历完，则相同
        if b == None:
            return True
        if a == None or a.val != b.val:
            return False
        return self.is_subTree(a.left, b.left) and self.is_subTree(a.right, b.right)
    

