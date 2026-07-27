from itertools import combinations
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product=1
        product*=(max(nums)-1)
        nums.remove(max(nums))
        product*=(max(nums)-1)
        return product
        