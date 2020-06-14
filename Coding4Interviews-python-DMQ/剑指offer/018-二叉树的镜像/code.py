

def Mirror(root):
    # write code here
    if not root:
        return None
    tmp = Mirror(root.right)
    root.right = Mirror(root.left)
    root.left = tmp
    return root、

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        # 递归
        if root:
            root.left,  root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)