
class Solution:
    # s Դ�ַ���
    def replaceSpace(self, s):
        # write code here
        # һ��python�����ⷨ
        #return s.replace(" ", "%20")
        # ����
        if not s:
            return ''
        l = ''
        for i in s:
            if i == ' ':
                l += '%20'
            else:
                l += i
        return l