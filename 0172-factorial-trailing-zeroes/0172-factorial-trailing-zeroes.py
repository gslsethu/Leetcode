import math
class Solution(object):
    def trailingZeroes(self, n):
        if n==0 or n==1:
            return 0
        if n>1:
            s=math.factorial(n)
        s=list(map(int,str(s)))
        count=0
        high=len(s)-1
        while high>=0:
            if s[high]==0:
                count+=1
                high-=1
            else:
                break
        return count

        
        