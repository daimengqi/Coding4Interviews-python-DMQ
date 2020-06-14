
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # 一、python暴力解法
        #return s.replace(" ", "%20")
        # 二、
        if not s:
            return ''
        l = ''
        for i in s:
            if i == ' ':
                l += '%20'
            else:
                l += i
        return l