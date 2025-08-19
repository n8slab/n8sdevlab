import math
import numpy as np
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans = np.inf
        summ = 0
        j = 0

        for i, num in enumerate(nums):
            summ += num
            while summ >= target:
                ans = min(ans, i - j + 1)
                summ -= nums[j]
                j += 1

        return 0 if ans == np.inf else ans