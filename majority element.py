
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
	return max(counts, key=counts.get)