class Solution(object):
    def checkDivisibility(self, n):
        s=0
        p=1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        if(n%(s+p)==0):
            return True
        else:
            return False
        
        