class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1

        return i

#        for num in nums:
#            while nums.count(num)>2:
#                nums.remove(num)
#        return len(nums)