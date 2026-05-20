class Solution(object):
    def permute(self, nums):
        from itertools import permutations
        res=list(permutations(nums))
        return res


        
        