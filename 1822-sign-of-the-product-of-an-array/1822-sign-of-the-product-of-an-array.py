class Solution(object):
    def signFunc(self,result):
        if result>0:
            return 1
        elif result==0:
            return 0
        else:
            return -1
    def arraySign(self, nums):
        result=1
        for i in range(len(nums)):
            result=result*nums[i]
        return self.signFunc(result)

        