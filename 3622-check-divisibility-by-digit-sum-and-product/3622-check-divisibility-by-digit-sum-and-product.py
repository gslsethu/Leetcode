class Solution(object):
    def checkDivisibility(self, n):
        temp=n
        s=0
        p=1
        for i in range(0,len(str(n))):
            digit=n%10
            s+=digit
            p*=digit
            n=n//10
            
        if(temp%(s+p)==0):
            return True
        else:
            return False
        
        