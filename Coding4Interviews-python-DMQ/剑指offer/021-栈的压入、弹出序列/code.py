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

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # ����һ������ջstack���� pushV���Ԫ�����μ��뵽ջ�У�����ջ��Ԫ����popV[0]�Ƚ�
        # ������ȣ��������pushV��Ԫ��ѹ��ջ�У�����ȣ���popV[0]�͸���ջ��Ԫ��һ��pop
        # �ٶ�ʣ���ջ��Ԫ�غ�popV��Ԫ�ؽ����ظ��Ƚϡ������ջΪ�ա������Ϊ��˵���������в��Ǹ�ջ�ĵ���˳��
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