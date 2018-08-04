# version_1 字符串
# class Solution:
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if str(x) == str(x)[::-1]:
#             return True
#         else:
#             return False

# version_2 不用字符串


class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        num = 0
        while x > num:
            num *= 10
            num += (x % 10)
            x //= 10
        return x == num or x == (num // 10)


while True:
    test = Solution()
    num = input()
    result = test.isPalindrome(int(num))
    print(result)
