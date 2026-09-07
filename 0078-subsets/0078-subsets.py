class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(i,current):
            if i==len(nums):
                ans.append(current[:])
                return
            backtrack(i+1,current)
            current.append(nums[i])
            backtrack(i+1,current)
            current.pop()
        backtrack(0,[])
        return ans
        