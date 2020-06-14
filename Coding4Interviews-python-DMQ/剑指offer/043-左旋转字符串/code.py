def reverse(str, s, e):
    e -= 1
    while s < e:
        str[s], str[e] = str[e], str[s]
        s += 1
        e -= 1

class Solution:

    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0 or n == 0: return s
        s = list(s)
        reverse(s, 0, n)
        reverse(s, n, len(s))
        reverse(s, 0, len(s))
        return ''.join(s)

print(Solution().LeftRotateString('abcdef', 3))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        # 一、python暴力解法
        # return s[n: ] + s[: n]
        if not s:
            return ''
        length = len(s)
        n = n % length
        s += s
        return s[n: n+length]