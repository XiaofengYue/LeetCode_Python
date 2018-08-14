class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_l = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list_l.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.list_l.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list_l[len(self.list_l) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list_l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
