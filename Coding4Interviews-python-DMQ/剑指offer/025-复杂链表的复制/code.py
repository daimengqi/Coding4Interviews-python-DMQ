class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 返回 RandomListNode
def Clone(pHead):
    # write code here
    if not pHead: return None
    p = pHead
    new_h = RandomListNode(p.label)
    pre_p = new_h
    random_map = {pHead: new_h}
    p = p.next
    while p:
        new_p = RandomListNode(p.label)
        random_map[p] = new_p
        pre_p.next = new_p
        pre_p = pre_p.next
        p = p.next
    p = pHead
    new_p = new_h
    while p:
        random_p = p.random
        if random_p:
            new_p.random = random_map[random_p]

        p = p.next
        new_p = new_p.next

    return new_h

p = RandomListNode(1)
p.next = RandomListNode(2)
p.next.next = RandomListNode(3)
p.next.next.next = RandomListNode(4)
p.next.next.next.next = RandomListNode(5)
print(Clone(p))

# 解法二
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 递归法：把大问题转化若干子问题
        # 此题转化为一个头结点和除去头结点剩余部分，剩余部分操作和原问题一致
        
        if not pHead:
            return None
        
        # 创建一个新节点
        p = RandomListNode(pHead.label)
        p.next = pHead.next
        p.random = pHead.random
        
        # 递归其他节点
        p.next = self.Clone(pHead.next)
        
        return p