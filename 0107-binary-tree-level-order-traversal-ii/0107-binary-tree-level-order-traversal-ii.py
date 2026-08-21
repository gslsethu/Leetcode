# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        def levelorder(root):
            if root is None:
                print([])
                return
            q = deque([root])
            while q:
                level = []
                n = len(q)
                for _ in range(n):
                    curr = q.popleft()
                    level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                result.append(level)
        levelorder(root)
        return result[::-1]


        