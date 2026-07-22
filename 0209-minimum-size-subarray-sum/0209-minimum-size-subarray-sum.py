class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        min_length=float('inf')
        csum=0
        if sum(nums)<target:
            return 0
        for right in range(len(nums)):
            csum+=nums[right]
            while csum>=target:
                min_length=min(min_length,right-left+1)
                csum-=nums[left]
                left+=1
        return min_length

            

        




        