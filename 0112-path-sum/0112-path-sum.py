# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        res=[]
        def dfs(root,path,total):
            if root is None:
                return 
            path.append(root.val)
            total+=root.val
            if root.left is None and root.right is None:
                if total==targetSum:
                    res.append(path[:])
            else:
                dfs(root.left,path,total)
                dfs(root.right,path,total)
        dfs(root,[],0)
        if len(res)!=0:
            return True
        return False
        
            
        