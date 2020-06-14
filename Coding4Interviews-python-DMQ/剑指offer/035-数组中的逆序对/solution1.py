
#  234 345
#  233445
def MergeElem(data, start, mid, end, temp):  # data[start...mid], data[mid+1...end]
    cnt = 0
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if data[j] < data[i]:  # data[start...i...mid] data[mid+1...j...end]
            temp[k] = data[j]
            cnt += j - k
            j += 1
            k += 1
        else:
            temp[k] = data[i]
            i += 1
            k += 1
    while i <= mid:
        temp[k] = data[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1
    data[start:end+1] = temp[start:end+1]
    return cnt

def InverseCore(data, start, end, temp):
    cnt = 0
    if start < end:
        mid = (start + end) // 2
        cnt += InverseCore(data, start, mid, temp)
        cnt += InverseCore(data, mid+1, end, temp)
        cnt += MergeElem(data, start, mid, end, temp)
    return cnt

def InversePairs(data):
    # write code here
    temp = data[:]
    count = InverseCore(data, 0, len(data)-1, temp)
    return count

print(InversePairs([1,2,3,5,4,6,7,0]))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0 
        # 辅助数组存储array中的元素，并排序
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        # 顺序遍历辅助数组，依次找到data数组中的最小元素；
        # 在data数组中，最小元素前面有多少个数，就有多少个逆序对；
        # 找到逆序对数后，data数组删除最小元素，继续遍历
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count%1000000007