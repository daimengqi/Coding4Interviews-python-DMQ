def biSearch(data, k):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > k:
            high = mid - 1
        elif data[mid] < k:
            low = mid + 1
    return high

def GetNumberOfK(data, k):
    # write code here
    if not data: return 0
    return biSearch(data, k+0.5) - biSearch(data, k-0.5)

print(GetNumberOfK([3,3,3, 4],3))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 一、python暴力解法
        # return data.count(k)
        # 二、遍历
        # count = 0
        # for i in range(len(data)):
            # if data[i] == k:
                # count += 1
        # return count
        # 三、二分查找
        if not data:
            return 0
        return self.findFirst(data, k, 0, len(data)-1)
    def findFirst(self, data, k, start, end):
        if start == end:
            if data[start] == k:
                return 1
            else:
                return 0 
        if data[start] == data[end] == k:
            return end-start+1
        mid = (start + end)/2
        return self.findFirst(data, k, start, mid) + self.findFirst(data, k, mid+1, end)
                
