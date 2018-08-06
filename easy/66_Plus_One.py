import re


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 数字数组转换成字符串转换int+1
        # 得到正确结果
        num = str(int(''.join(list(map(str, digits)))) + 1)
        # 将int转换成数组
        return list(map(int, re.findall('\d', num)))
