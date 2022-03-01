class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [0]
        
        for i in range(1, n+1):
            results.append(results[i & (i-1)] + 1)
            
        return results