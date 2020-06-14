    

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        s = '^' + s 
        pattern = '^' + pattern
        i = len(s) - 1
        j = len(pattern) - 1
        star_match = False
        while i>=0 and j>=0:
            if star_match:
                if pattern[j] == '.' or pattern[j] == s[i]:
                    if self.match(s[1:i], pattern[1:j]):  # 先靠前匹配，从1开始是去掉index为0的^
                        return True
                    else:
                        i -= 1
                else:
                    j -= 1
                    star_match = False
            else:
                if s[i] == pattern[j] or pattern[j] == '.':
                    i -= 1
                    j -= 1
                elif pattern[j] == '*':
                    star_match = True
                    j -= 1
                else:
                    return False
        return (i == -1 and j == -1)


print(Solution().match('aa', 'a*'))

# 解法二
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # 如果s和pattern都为空
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果s不为空，pattern为空
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # 如果s为空，pattern不为空
        elif len(s) == 0 and len(pattern) != 0:
            # 如果pattern第二位是*
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # s与pattern都不为空
        else:
            # 如果pattern第二位是*
            if len(pattern) > 1 and pattern[1] == '*':
                # 如果s[0]与pattern[0]不同，只有当pattern前两位为空，把pattern后移两位
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                # 如果s[0]与pattern[0]相同，且pattern[1] == '*',有三种情况：
                # 1.pattern前两位为空，pattern 后移两位
                # 2.pattern前两位不为空，且与s[0]匹配
                # 3.*表示多位的时候，pattern不变，s后移一位，相当于pattern前两位可以与s中的多个字符匹配
                else:
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # 如果pattern第二位不是*
            else:
                # 当且仅当s[0]与pattern[0]相同，后续存在匹配的可能
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False