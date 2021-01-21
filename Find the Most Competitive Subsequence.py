#Find the Most Competitive Subsequence

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        n = len(nums)
        for i,num in enumerate(nums):
            while stack and stack[-1]>num and (n-i)+len(stack)>k:
                stack.pop()
            stack.append(num)
        return stack[0:k]