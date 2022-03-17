class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
	score = 0
	for c in s:
		if c =='(':
		    stack.append(0)
		else:
			v = stack.pop()
			stack[-1]+= max(v * 2, 1)
	return sum(stack)