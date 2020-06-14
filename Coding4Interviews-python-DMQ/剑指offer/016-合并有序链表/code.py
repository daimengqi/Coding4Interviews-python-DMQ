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

# �ⷨ��
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # ���غϲ����б�
    def Merge(self, pHead1, pHead2):
        # write code here
        # �½�һ��ͷ�ڵ㣬������ϲ�������
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
        # ��δ�������������ӵ��ϲ��������β��,���ڶ�������Ϊ��
        if pHead1:
            head.next = pHead1
        # ����һ������Ϊ��
        elif pHead2:
            head.next = pHead2
        return merge.next
