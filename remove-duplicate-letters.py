class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
		counter = Counter(s)
        result = []  # need to form an ascending order
        visited = defaultdict(bool)  # dedup purposes
        
        for char in s:
            counter[char] -= 1
            if visited[char]:
                continue
                
            while result and counter[result[-1]] and result[-1]>char:
                # the condiction counter[result[-1]] is really important.
                # because it makes unique letter stay in the result.
                # no matter the lexical order.
                # appearance is more important than lexical order.
                item = result.pop()
                visited[item]=False
            
            visited[char] = True
            result.append(char)
            
        return "".join(result)				