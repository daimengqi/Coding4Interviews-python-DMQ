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

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0 # 计数
    # 思路：BFS,先将地图全部设置为1，遍历到的方格置为0，并计数+1。
    # 这个思路在找前后左右相连的点很有用，比如leetcode中的海岛个数问题/最大海岛问题都可以用这种方法来求解。
    def movingCount(self, threshold, rows, cols):
        # write code here
        #  将地图即二维矩阵置为1
        array = [[1 for i in range(cols)] for j in range(rows)]
        self.find_way(array, 0, 0, threshold)
        return self.count
        
    def find_way(self, array, i, j, k):
        if i<0 or j<0 or i>= len(array) or j>= len(array[0]):
            return 
        tmp_i = list(map(int, str(i))) # 将数值变为字符串，并将字符串中字符转为int，添加到list中
        tmp_j = list(map(int, str(j))) # 为了方便调用list的sum方法，计算数位和
        if sum(tmp_i) + sum(tmp_j) > k or array[i][j] != 1 : #机器人不进入数位和大于K，或者方格已经到达过的方格
            return
        array[i][j] = 0
        self.count += 1
        self.find_way(array, i-1, j ,k)
        self.find_way(array, i+1, j ,k)
        self.find_way(array, i, j-1 ,k)
        self.find_way(array, i, j+1 ,k)
