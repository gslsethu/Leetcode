class Solution(object):
    def singleNumber(self, nums):
        a = 3*sum(set(list(nums))) - sum(nums)
        return (a)//2

        
        