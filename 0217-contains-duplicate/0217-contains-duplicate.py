class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=list(set(nums))
        if len(nums)==len(l):
            return False
        else:
            return True
        