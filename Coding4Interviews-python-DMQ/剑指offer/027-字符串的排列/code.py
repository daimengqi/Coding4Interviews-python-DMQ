
def helper(s):
    if len(s) == 1:
        return s[0]
    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])
        for j in l:
            res.append(s[i] + j)

    return res

def Permutation(ss):
    # write code here
    if not ss: return []
    words = list(ss)
    return list(sorted(set(helper(words))))

print(Permutation('aa'))

# 解法二
# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        result = []
        # 返回可迭代对象的所有数学全排列方式
        res = itertools.permutations(ss)
        for i in res:
                result.append("".join(i))
        result = list(set(result))
        result.sort()
        return result
                    
