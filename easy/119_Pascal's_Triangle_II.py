class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = [1]

        for i in range(1, rowIndex + 1):
            a.append(1)
            for j in range(i - 1, 0, -1):
                a[j] += a[j - 1]
        return a
