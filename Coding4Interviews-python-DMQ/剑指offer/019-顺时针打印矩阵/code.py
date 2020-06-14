def printMatrix(matrix):
    # write code here
    walked = [[False] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
    for j in range(len(walked[-1])):
        walked[-1][j] = True
    for i in range(len(walked)):
        walked[i][-1] = True
    len_row = len(matrix) - 1
    len_col = len(matrix[0]) - 1
    res = []
    i = 0
    j = 0
    direction = 0  # 0向右，1向下，2向左，3向上

    while not walked[i][j]:
        res.append(matrix[i][j])
        walked[i][j] = True
        if direction == 0: # right
            if j < len_col and not walked[i][j+1]:
                j += 1
            else:
                direction = 1
                i += 1
        elif direction == 1: # down
            if i < len_row and not walked[i+1][j]:
                i += 1
            else:
                direction = 2
                j -= 1
        elif direction == 2:  # left
            if j > 0 and not walked[i][j-1]:
                j -= 1
            else:
                direction = 3
                i -= 1
        elif direction == 3:  # up
            if i > 0 and not walked[i-1][j]:
                i -= 1
            else:
                direction = 0
                j += 1
    return res

print(printMatrix([[1,2],[3,4]]))
print(printMatrix([[1]]))
    
# 解法二
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 魔方逆时针旋转问题：pop矩阵第一行到结果数组，再对剩余矩阵进行逆时针旋转，重复上述步骤
        result = []
        while matrix:
            result += matrix.pop(0)
            if len(matrix) == 0 :
                break
            matrix = self.tranverse(matrix)
        return result
    # 逆时针翻转矩阵
    def tranverse(self, matrix):
        row_num = len(matrix)
        col_num = len(matrix[0])
        newMatrix= []
        for c in range(col_num):
            row = []
            for r in range(row_num):
                row.append(matrix[r][c])
            newMatrix.append(row)
        newMatrix.reverse()
        return newMatrix