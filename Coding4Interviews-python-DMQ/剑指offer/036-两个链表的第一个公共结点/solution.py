class Solution(object):
    def getIntersectionNode(self, pHead1, pHead2):
        p1, n_p1 = pHead1, 0
        p2, n_p2 = pHead2, 0
        while p1:
            p1 = p1.next
            n_p1 += 1
        while p2:
            p2 = p2.next
            n_p2 += 1
        if n_p1 < n_p2:     # p1指向长链
            pHead1, pHead2 = pHead2, pHead1
            n_p1, n_p2 = n_p2, n_p1

        for _ in range(n_p1 - n_p2):
            pHead1 = pHead1.next
        while pHead1 and pHead2:
            if pHead1 == pHead2:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return None

# 解法二
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        p1 = pHead1
        p2 = pHead2
        # 遍历第一个链表，将节点值存入list1
        while p1:
            list1.append(p1.val)
            p1 = p1.next
        # 遍历第二个链表，看是否存在公共值
        while p2:
            if p2.val in list1:
                return p2
            else:
                p2 = p2.next
