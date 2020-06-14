class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        else:
            if self.min_stack[-1] < node:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(node)
    def pop(self):
        # write code here
        self.stack.pop(-1)
        self.min_stack.pop(-1)
    
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return []

    def min(self):
        # write code here
        return self.min_stack[-1]
        

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        # �洢stack�е���СԪ�ص�ջ
        self.minStack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        # ѹջ����ԭ����СԪ�ر�Ϊ��СԪ��
        if not self.minStack or self.minStack[-1] > node:
            self.minStack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minStack[-1]