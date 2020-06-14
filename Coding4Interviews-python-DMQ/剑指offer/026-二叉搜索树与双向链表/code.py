# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pre = None
        
    def Convert(self, root):
        # write code here
        if not root: return None
        self.helper(root)
        while root.left:
            root = root.left
        return root

    def helper(self, cur):
        if not cur: return None
        self.helper(cur.left)
        cur.left = self.pre
        if self.pre:
            self.pre.right = cur
        self.pre = cur
        self.helper(cur.right)

# 解法二
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 新建数组 存储树节点，也是存储双向链表
    def __init__(self):
        self.arr = []
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        # 二叉搜索树，中序遍历将树节点顺序存储
        self.midTraversal(pRootOfTree)
        # 双向链表中指针数比元素个数少一
        for i, v in enumerate(self.arr[: -1]):
            # 双向链表，节点的右孩子也是链表中指向的下一个节点
            v.right = self.arr[i+1]
            # 双向链表，节点的左孩子也是链表中上一个节点
            self.arr[i+1].left = v
        # 数组存储顺序树节点，同时也是双向链表。知道树的根节点，即获得链表的标头，也就能获得整个双向链表
        return self.arr[0]
    # 中序遍历存储树的节点
    def midTraversal(self,root):
        if not root:
            return None
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)
        
