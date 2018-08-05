class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        list_l = []
        list_l.append('')
        list_l.append('1')
        for i in range(1, n):
            sum = 0
            num = list_l[i][0]
            str_result = ''
            for j in list_l[i]:
                if j == num:
                    sum += 1
                else:
                    str_result = str_result + str(sum) + num
                    sum = 1
                    num = j
            str_result = str_result + str(sum) + num
            list_l.append(str_result)
        return list_l[n]
