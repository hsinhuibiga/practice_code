class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        
        while columnNumber > 0:
            columnNumber -= 1  # 26 -> "Z"
            res += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return res[::-1]