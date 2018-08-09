class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_l = []
        for i in range(numRows):
            ll = [1] * (i + 1)
            list_l.append(ll)

            if i > 1:
                for j in range(1, i):
                    list_l[i][j] = list_l[i - 1][j - 1] + list_l[i - 1][j]

        return list_l
