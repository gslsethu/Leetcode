class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        maxi = 1
        curr = 1
        if len(nums)==0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                maxi = max(maxi, curr)
                curr = 1
        maxi = max(maxi, curr)
        return maxi
        
        
        