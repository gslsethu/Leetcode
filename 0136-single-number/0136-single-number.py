class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=sum(nums)-2*(sum(set(nums)))
        return -d
        