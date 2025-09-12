class Solution(object):
    def removeDuplicates(self, nums):
        s=list(set(nums))
        s.sort()
        for i in range(len(s)):
            nums[i]=s[i]
            
        return len(s)
             

        
        
        