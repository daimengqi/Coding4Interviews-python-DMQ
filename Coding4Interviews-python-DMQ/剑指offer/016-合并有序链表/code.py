class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(pHead1, pHead2):
    # write code here
    res = ListNode(0)
    head = res
    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            head.next = pHead1
            head = head.next
            pHead1 = pHead1.next
        else:
            head.next = pHead2
            head = head.next
            pHead2 = pHead2.next
            
    if pHead1:
        head.next = pHead1
    if pHead2:
        head.next = pHead2
    return res.next

# 解法二
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # 新建一个头节点，用来存合并的链表
        head = ListNode(90)
        merge = head
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next
        # 把未结束的链表连接到合并后的链表尾部,若第二个链表为空
        if pHead1:
            head.next = pHead1
        # 若第一个链表为空
        elif pHead2:
            head.next = pHead2
        return merge.next
