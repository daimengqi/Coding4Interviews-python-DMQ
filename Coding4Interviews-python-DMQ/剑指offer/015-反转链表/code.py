class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    # write code here

    if not pHead: return None
    head = ListNode(0)
    head.next = pHead
    p = pHead
    while(p.next):
        tp = p.next
        p.next = p.next.next
        tp.next = head.next
        head.next = tp
    return head.next


    # head->4->3->2->1->5
    #                p  tp
   
# �ⷨ��
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # ����ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        # ��������βָ��
        last = None
        while pHead:
            # ��������һ�����
            tmp = pHead.next
            # ��ͷ�ڵ�ָ��ԭ������β
            pHead.next = last
            # ԭ������β���ͷ�ڵ�
            last = pHead
            # ���б���
            pHead = tmp
        return last