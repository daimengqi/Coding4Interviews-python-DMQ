class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode: return None
        p = pNode
        if pNode.right:  # 有右子树
            p = pNode.right
            while p.left:
                p = p.left
            return p
         # 没有右子树但是有父亲节点
        while pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
        return pNode.next

# 解法二
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        #1.二叉树为空
        if not pNode:
            return None
        #2.如果该节点存在右孩子，则它的下一个节点是找到其右孩子并沿着右孩子的左孩子一路向下找，找到最左边的节点
        if pNode.right:
            res = pNode.right
            while res.left:
                res = res.left
            return res
        #3.如果该节点不存在右孩子，若它是其父亲节点的左孩子，则下一个节点是其父节点；否则，继续向上遍历父节点的父节点，重复上述判断，并返回结果
        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            pNode = temp
        return None