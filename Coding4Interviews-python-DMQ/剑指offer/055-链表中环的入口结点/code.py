class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        head = ListNode(0)
        head.next = pHead
        fast = head
        slow = head
        while True:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                fast = head
                break
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

# 解法二
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 遍历链表，环的存在，遇见的第一个重复点就是入口结点
        tempList = []
        p = pHead
        while p :
            if p in tempList:
                return p 
            else:
                tempList.append(p)
            p = p.next