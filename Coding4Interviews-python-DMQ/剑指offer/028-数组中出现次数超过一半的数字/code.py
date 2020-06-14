def MoreThanHalfNum_Solution(numbers):
    # write code here
    res = None
    cnt = 0
    for i in numbers:  # 留下数组中出现次数最高的数
        if not res:
            res = i
            cnt = 1
        else:
            if i == res:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res = None
    # 判断次数是否大于一半
    cnt = 0 
    for i in numbers:
        if i == res:
            cnt += 1
    if cnt > len(numbers) / 2:
        return res
    else:
        return 0

print(MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 一、dict法，时间复杂度O(n)
        dict={}
        for i in numbers:
            if not dict.has_key(i):
                dict[i] = 1
            else:
                dict[i] += 1
            if dict[i] > len(numbers)/2 :
                return i
        return 0
        # 二、python暴力解法：数组排序后，如果符合条件的数存在，则一定是数组中间那个数
#        numbers.sort()
#        thenum = numbers[len(numbers)/2]
#        if numbers.count(thenum) > len(numbers)/2 :
#            return thenum
#        return 0 