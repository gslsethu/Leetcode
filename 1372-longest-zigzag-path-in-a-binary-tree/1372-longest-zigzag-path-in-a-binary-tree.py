# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return (-1,-1)
            l=dfs(node.left)
            r=dfs(node.right)
            left=l[1]+1
            right=r[0]+1
            ans=max(ans,left,right)
            return left,right
        dfs(root)
        return ans
        