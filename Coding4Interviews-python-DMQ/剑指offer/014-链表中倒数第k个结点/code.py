class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FindKthToTail(head, k):
    # write code here
    if not head: return None
    fast_p = head
    slow_p = head
    for _ in range(k):
        if fast_p:
            fast_p = fast_p.next
        else:
            return None
    while fast_p:
        fast_p = fast_p.next
        slow_p = slow_p.next
    return slow_p

# ½â·¨¶þ
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        List = []
        while head != None:
            List.append(head)
            head = head.next
        if k < 1 or k > len(List):
            return None
        else:
            return List[-k]
