class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        while left<=right:
            mid=(left+right)//2
            total=0
            parts=1
            for num in nums:
                if total+num>mid:
                    parts+=1
                    total=num
                else:
                    total+=num
            if parts<=k:
               right=mid-1
            else:
               left=mid+1
        return left
            
            
        