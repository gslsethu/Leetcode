class Solution(object):
    def longestConsecutive(self, nums):
        nums=set(nums)
        longest=0
        
        for num in nums:
            if num-1 not in nums:
                curr=num+1
                length=1
                while curr in nums:
                    curr+=1
                    length+=1
                longest=max(longest,length)
        return longest

        
        
        
        