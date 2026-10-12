class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={}
        for i,ch in enumerate(s):
            last[ch]=i
        ans=[]
        start=end=0
        for i,ch in enumerate(s):
            end=max(end,last[ch])
            if i==end:
                ans.append(end-start+1)
                start=i+1
        return ans

        