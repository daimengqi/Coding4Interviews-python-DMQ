def FindGreatestSumOfSubArray(array):
    # write code here
    max = array[0]
    dp = [0] * (len(array) + 1)
    dp[0] = array[0]
    for i in range(1, len(array)):
        if dp[i-1] < 0:
            dp[i] = array[i]
        else:
            dp[i] = array[i] + dp[i-1]
        if dp[i] > max:
            max = dp[i]
    return max


print(FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # 动态规划，dp[i]表示以array[i]结尾的序列的最大连续子向量和
        # dp[i] = max(dp[i-1]+array[i], array[i])
        dp = [ i for i in array]
        for i in range(1, len(array)):
            dp[i]=max(dp[i-1]+array[i], array[i])
        return max(dp)