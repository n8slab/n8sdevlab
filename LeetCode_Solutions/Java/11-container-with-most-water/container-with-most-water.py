class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curMax = 0
        l = 0
        r = len(height)-1

        while l<r:
            high = min(height[l], height[r])
            curMax = max(curMax, high*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return curMax
