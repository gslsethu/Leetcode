class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def backtrack(start,current):
            if start==len(s):
                ans.append(current[:])
                return
            for end in range(start+1,len(s)+1):
                part=s[start:end]
                if part==part[::-1]:
                    current.append(part)
                    backtrack(end,current)
                    current.pop()
        backtrack(0,[])
        return ans
            
        