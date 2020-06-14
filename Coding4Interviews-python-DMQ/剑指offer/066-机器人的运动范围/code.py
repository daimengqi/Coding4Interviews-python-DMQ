class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        rows = m
        cols = n
        threshold = k
        array = []
        for i in range(rows):
            res = []
            for j in range(cols):
                res.append(getN(i, j))
            array.append(res)
        visited = [[0] * len(array[0]) for _ in range(len(array))]
        return BFS(array, 0, 0, threshold, visited)

def getN(i, j):
    res = 0
    while i:
        res += (i % 10)
        i //= 10
    while j:
        res += (j % 10)
        j //= 10
    return res

def BFS(array, i, j, threshold, visited):
    if i<0 or j<0 or i>len(array)-1 or j>len(array[0])-1 or array[i][j]>threshold or visited[i][j]:
        return 0
    res = 1
    visited[i][j] = 1
    res += BFS(array, i+1, j, threshold, visited)
    res += BFS(array, i-1, j, threshold, visited)
    res += BFS(array, i, j+1, threshold, visited)
    res += BFS(array, i, j-1, threshold, visited)
    return res

# �ⷨ��
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0 # ����
    # ˼·��BFS,�Ƚ���ͼȫ������Ϊ1���������ķ�����Ϊ0��������+1��
    # ���˼·����ǰ�����������ĵ�����ã�����leetcode�еĺ�����������/��󺣵����ⶼ���������ַ�������⡣
    def movingCount(self, threshold, rows, cols):
        # write code here
        #  ����ͼ����ά������Ϊ1
        array = [[1 for i in range(cols)] for j in range(rows)]
        self.find_way(array, 0, 0, threshold)
        return self.count
        
    def find_way(self, array, i, j, k):
        if i<0 or j<0 or i>= len(array) or j>= len(array[0]):
            return 
        tmp_i = list(map(int, str(i))) # ����ֵ��Ϊ�ַ����������ַ������ַ�תΪint����ӵ�list��
        tmp_j = list(map(int, str(j))) # Ϊ�˷������list��sum������������λ��
        if sum(tmp_i) + sum(tmp_j) > k or array[i][j] != 1 : #�����˲�������λ�ʹ���K�����߷����Ѿ�������ķ���
            return
        array[i][j] = 0
        self.count += 1
        self.find_way(array, i-1, j ,k)
        self.find_way(array, i+1, j ,k)
        self.find_way(array, i, j-1 ,k)
        self.find_way(array, i, j+1 ,k)
