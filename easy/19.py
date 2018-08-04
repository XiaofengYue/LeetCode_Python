class Solution:
    def romanToInt(self, s):
        """
        :type x: int
        :rtype: bool
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0
        for index, value in enumerate(s):
            sum += dic[value]
            if (index != 0 and dic[s[index]] > dic[s[index - 1]]):
                sum -= dic[s[index - 1]] * 2
        return sum


while True:
    test = Solution()
    num = input()
    result = test.romanToInt(num)
    print(result)
