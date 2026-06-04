class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return None
        if len(nums)<2:
            return nums
        if len(nums)==2:
            if nums[0]!=nums[1]:
                return nums
            else:
                return None
        ans=[]
        if len(nums)>2:
            for i in nums:
                if nums.count(i)==1:
                    ans.append(i)
            return ans

