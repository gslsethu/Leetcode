class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans=0
        for i in range(32):
            x=(a>>i)&1
            y=(b>>i)&1
            z=(c>>i)&1
            if z==1:
                if x==0 and y==0:
                    ans+=1
            else:
                ans+=x+y
        return ans
        