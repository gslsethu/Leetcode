class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        
        res=list(permutations(nums))
        num=list(set(res))
        return num
        