def jumpFloorII(number):
    # write code here
    f1 = 1
    if number == 1: return f1
    for _ in range(number-1):
        f1 = 2*f1
    return f1
    
# 解法二
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 总结出f(n)=2*f(n-1)(n>=2)
        if number <= 0:
            return 0
        else:
            return pow(2, number-1)