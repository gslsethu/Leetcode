class Solution(object):
    def rotate(self, nums, k):
        
        
        if k==0:
            return nums
        n=len(nums)
        k=k%n
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        return nums

        