def rectCover(number):
    # write code here
    f1 = 1
    f2 = 2
    if number == 1: return f1
    if number == 2: return f2
    for _ in range(number-2):
        f2, f1 = f1 + f2, f2
    return f2

print(rectCover(3))

# 解法二
class Solution:
    def rectCover(self, number):
        # write code here
        # 斐波那契
        
        res = [0,1,2,3]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]