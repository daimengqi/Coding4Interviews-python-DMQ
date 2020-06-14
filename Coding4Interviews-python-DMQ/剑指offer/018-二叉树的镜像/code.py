

def Mirror(root):
    # write code here
    if not root:
        return None
    tmp = Mirror(root.right)
    root.right = Mirror(root.left)
    root.left = tmp
    return root��

# �ⷨ��
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ���ؾ������ĸ��ڵ�
    def Mirror(self, root):
        # write code here
        # �ݹ�
        if root:
            root.left,  root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)