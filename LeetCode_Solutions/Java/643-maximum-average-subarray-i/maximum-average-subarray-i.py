class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curSum = sum(nums[:k])
        curMax = curSum

        for i in range(k, len(nums)):
            curSum += (nums[i] - nums[i-k])
            curMax = max(curMax, curSum)
        
        return curMax/float(k)