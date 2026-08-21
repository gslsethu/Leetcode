# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        l=[]
        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        mini=float("inf")
        for i in range(1, len(l)):
            diff = l[i] - l[i-1]
            mini=min(mini,diff)
        return mini
  
       
       
        