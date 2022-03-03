class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive=0
        num=0
	for i in range (2,len(nums)):
		    if nums[i-1]-nums[i-2]==nums[i]-nums[i-1]:
		        consecutive+=1
			num+=consecutive
		    else: consecutive=0
			
	return num