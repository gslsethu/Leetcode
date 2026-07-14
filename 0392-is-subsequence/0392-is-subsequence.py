class Solution(object):
    def isSubsequence(self, s, t):
        left=0
        right=0
        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                left+=1
                right+=1
            else:
                right+=1
        if left==len(s):
            return True
        else: 
            return False
        
       
                

        
        