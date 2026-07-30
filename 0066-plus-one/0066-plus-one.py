class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=int(''.join(map(str,digits)))
        n=n+1
        digits=list(map(int,str(n)))
        return digits
        


        