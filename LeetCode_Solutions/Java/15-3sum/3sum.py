class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []

        ans = []

        nums.sort()

        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i +1
            r = len(nums)-1
            
            while l<r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
                elif sum3 < 0:
                    l+=1
                else:
                    r-=1
        return ans