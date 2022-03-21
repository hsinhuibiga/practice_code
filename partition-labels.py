class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """   
        # Init
        start = 0
        end = 0
        end_idx = [0 for _ in range(26)]
        results = []
        
        # Record the last position of character
        for i in range(len(s)):
            end_idx[ord(s[i])-ord('a')] = i
        
        # Scanning string character
        for i in range(len(s)):
            end = max(end, end_idx[ord(s[i])-ord('a')])
            
            if i == end:
                results.append(i-start+1)
                start = i + 1

        return results
