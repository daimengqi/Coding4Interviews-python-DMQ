def IsPopOrder(pushV, popV):
    # write code here
    stack = []
    i = 0
    for v in pushV:
        stack.append(v)
        while stack and stack[-1] == popV[i]:
            i += 1
            stack.pop(-1)
    if not stack:
        return True
    else:
        return False
    

print(IsPopOrder([1, 2, 3, 4, 5], [4,3,5,1,2]))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # 创建一个辅助栈stack，将 pushV里的元素依次加入到栈中，并将栈顶元素与popV[0]比较
        # 若不想等，则继续将pushV中元素压入栈中，若相等，则将popV[0]和辅助栈顶元素一起pop
        # 再对剩余的栈中元素和popV中元素进行重复比较。最后辅助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序
        stack = []
        if not pushV or len(pushV) != len(popV):
            return False
        for i in pushV:
            stack.append(i)
            while len(stack) and (stack[-1] == popV[0]):
                stack.pop()
                popV.pop(0)
        if len(stack):
                return False
        return True