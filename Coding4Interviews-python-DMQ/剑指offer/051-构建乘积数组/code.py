class Solution:
    def multiply(self, A):
        # write code here
        B = [1] * len(A)
        temp = 1
        for i in range(1, len(A)):
            temp *= A[i-1]
            B[i] *= temp
        temp = 1
        for i in range(len(A)-2, -1, -1):
            temp *= A[i+1]
            B[i] *= temp
        return B


# [0, 1, 1]
# [1, 0, 1]
# [1, 1, 0]

# ½â·¨¶þ
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = [1]*len(A)
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if i != j:
                    B[j] *= A[i]
        return B