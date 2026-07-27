from itertools import combinations
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=[]
        l.append(max(nums)-1)
        nums.remove(l[0]+1)
        l.append(max(nums)-1)
        return prod(l)
        