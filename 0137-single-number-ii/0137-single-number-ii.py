class Solution(object):
    def singleNumber(self, nums):
        a = sum(nums) - 3*sum(set(list(nums)))
        return (-a)//2

        
        