def FirstNotRepeatingChar(s):
    # write code here
    map = {}
    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1
    for i in range(len(s)):
        if map[s[i]] == 1:
            return i
    return -1

print(FirstNotRepeatingChar('abac'))

# ½â·¨¶þ
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)<=0 or len(s)>10000:
            return -1
        for i,v in enumerate(s):
            if s.count(v) == 1:
                return i