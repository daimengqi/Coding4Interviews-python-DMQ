# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        # 自定义排序规则：将a和b转为str后，若 a＋b<b+a， 就让a在前，b在后。
        # 即[a,b]为顺序排列，对应sorted()函数为排序方式为默认的false,升序
        if not numbers:
            return ''
        # 将整数依次转为字符串并加入到字符串数组
        strnum = [str(numbers[i]) for i in range(len(numbers))]
        # 按照自定义排序规则将字符串数组进行排序
        strnum.sort(self.compare)
        # 拼接字符串并转为整数
        return int(''.join(strnum))
    def compare(self, a, b):
        if a + b < b + a:
            return -1
        if a + b > b + a:
            return 1
        else:
            return 0 