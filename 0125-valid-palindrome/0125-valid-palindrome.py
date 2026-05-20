class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        st=""
        for i in range(len(s)):
            if ('a'<=s[i]<='z') or ('0'<=s[i]<='9'):
                st+=s[i]
        temp=st[::-1]
    
        if temp==st:
            return True
        else:
            return False