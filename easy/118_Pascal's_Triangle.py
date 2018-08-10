class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        list_l = [1]

        for i in range(1, rowIndex):
            for j in range(1, i + 1):
                if j >= i:
                    list_l.append(1)
                else:
                    list_l[j] = list_l[i - 1] + list_l[i]
        return list_l
