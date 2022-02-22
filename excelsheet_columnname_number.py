class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result =0
        n= len(columnTitle)
        for i in range(n):
            result=result*26+ord(columnTitle[i])-64
        return result