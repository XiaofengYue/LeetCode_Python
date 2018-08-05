class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and len(stack) != 0 and parmap[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False


while True:
    test = Solution()
    string = input()
    result = test.isValid(string)
    print(result)
