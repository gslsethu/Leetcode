# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(root,path,total):
            if root is None:
                return 0
            path.append(root.val)
            total+=root.val
            if root.left is None and root.right is None:
                if total==targetSum:
                    res.append(path[:])
            else:
                dfs(root.left,path,total)
                dfs(root.right,path,total)
            path.pop()
        
        dfs(root,[],0)
        return res
        
    
    