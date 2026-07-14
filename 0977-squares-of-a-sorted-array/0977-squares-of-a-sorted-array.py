class Solution(object):
    def sortedSquares(self, nums):
        l=[]
        for i in nums:
            l.append(i*i)
        l.sort()
        return l


        
        