class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
		stack = [ ]
		pi = 0
		for i in pushed:
		    stack.append(i)
			while stack and stack[-1]== popped[pi]:
				stack.pop()
			    pi += 1		
		return not stack