class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        count=0
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
                return
            if grid[r][c]=='0':
                return 
            grid[r][c]='0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    count+=1
                    dfs(r,c)  
        return count      