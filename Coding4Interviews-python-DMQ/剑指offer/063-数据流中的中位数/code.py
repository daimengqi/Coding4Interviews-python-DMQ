class Solution:
    def __init__(self):
        self.sortedList = []
    def Insert(self, num):
        # write code here
        n = len(self.sortedList)
        self.sortedList.append(num)
        while n != 0:
            if self.sortedList[n] < self.sortedList[n-1]:
                self.sortedList[n], self.sortedList[n-1] = self.sortedList[n-1], self.sortedList[n]
            else:
                break
            n -= 1
        if n == 0:
            self.sortedList[n] = num

    def GetMedian(self, x):
        # write code here
        n = len(self.sortedList)
        if n % 2 == 0:
            return (self.sortedList[n//2]+self.sortedList[n//2-1]) / 2.0
        else:
            return self.sortedList[n//2]
	
# ½â·¨¶þ
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sortedList = []
    def Insert(self, num):
        # write code here
        self.sortedList.append(num)
        self.sortedList.sort()
    def GetMedian(self, sortedList):
        # write code here
        length = len(self.sortedList)
        if length % 2 == 0:
            return (self.sortedList[length//2] + self.sortedList[length//2 - 1] ) / 2.0
        else:
            return self.sortedList[length//2]