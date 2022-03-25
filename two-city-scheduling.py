class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Init
        total = 0
        diff = []
        
        # All people go to city A
        for cost in costs:
            total += cost[0]
            diff.append(cost[1]-cost[0])
            
        # Sort
        diff.sort()
        
        # Balance
        for i in range(len(costs)//2):
            total += diff[i]
        
        return total
