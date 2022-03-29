class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count= collections.Counter(nums)
        for n in count:
            if count[n] > 1:
                return n