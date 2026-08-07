class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h, ans = [0]*len(matrix[0]), 0
        for row in matrix:
            for i in range(len(h)):
                h[i] = h[i]+1 if row[i] == "1" else 0
            s = [-1]
            for i in range(len(h)+1):
                x = h[i] if i < len(h) else 0
                while s[-1] != -1 and x < h[s[-1]]:
                    j = s.pop()
                    ans = max(ans, h[j]*(i-s[-1]-1))
                s.append(i)
        return ans
        