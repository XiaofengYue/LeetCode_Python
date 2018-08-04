import math


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != '-':
            str_x = str_x[::-1]
        else:
            str_x = str_x[:0:-1]
            str_x = '-' + str_x
        if -2147483648 < int(str_x) < 2147483647:
            return int(str_x)
        return 0


while True:
    print(math.pow(2, 31))
    test = Solution()
    num = input()
    result = test.reverse(int(num))
    print(result)
