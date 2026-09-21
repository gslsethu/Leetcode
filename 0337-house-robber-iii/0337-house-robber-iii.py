# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dp(node):
            if not node:
                return [0,0]
            l=dp(node.left)
            r=dp(node.right)
            rob=node.val+l[1]+r[1]
            skip=max(l)+max(r)
            return [rob,skip]
        return max(dp(root))
        
        