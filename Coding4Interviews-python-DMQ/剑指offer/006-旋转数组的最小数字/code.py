class Solution(object):
    def minArray(self, numbers):
        low, high = 0, len(numbers) - 1
        while low < high:
            mid = (high+low) / 2
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                if (numbers[high - 1] > numbers[high]):  # 确保正确的下标
                    low = high
                    break
                high -= 1  # 如果numbers[hign-1]=numbers[high]的情况
        return numbers[low]

# 解法二
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0 :
            return 0
        min = rotateArray[0]
        for i in range(0,len(rotateArray)):
            current = rotateArray[i]
            if current < min:
                min = current
                break
        return min
