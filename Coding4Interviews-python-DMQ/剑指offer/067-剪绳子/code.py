# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        # 一、贪心算法
        # 首先举例证明，当n>=4 的时候，分成求最大值的m段中，每段绳长只能是由2或者3构成
        # 且2的个数肯定小于3个，因为2*2*2<3*3
        # 因此可以主要看分成的3的个数，按照除以3取余
        if number == 2:
            return 1
        elif number == 3:
            return 2
        else:
            x = number % 3
            if x == 0:
                return pow(3, number//3)
            if x == 1:
                return 2*2*pow(3, number//3 - 1)
            else:
                return 2*pow(3, number//3)
                