class Solution(object):
    def missingNumber(self, nums):
        for i in range(0,len(nums)+1):
            if i in nums:
                continue
            else:
                return i
        