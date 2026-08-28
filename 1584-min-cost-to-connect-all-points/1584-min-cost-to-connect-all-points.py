class dsu:
    def __init__(self,n):
        self.parent=list(range(n+1))
    def find(self,x):
        if self.parent[x]==x:
            return x
        return self.find(self.parent[x])
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if py==px:
            return False
        self.parent[py]=px
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost=0
        edges=[]
        DSU=dsu(len(points))
        for i in range(len(points)):
            for j in range(i,len(points)):
                x1,y1=points[i]
                x2,y2=points[j]
                w=abs(x1-x2)+abs(y1-y2)
                edges.append([i,j,w])
        edges.sort(key=lambda x:x[2])
        for i,j,w in edges:
            if DSU.union(i,j):
                cost+=w
        return cost
        

        