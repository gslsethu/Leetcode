# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        l=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        l.sort()
        r=[0]
        

        def change(root):
            if root is None:
                return 
            change(root.left)
            root.val=l[r[0]]
            r[0]+=1
            change(root.right)
        change(root)
        
        