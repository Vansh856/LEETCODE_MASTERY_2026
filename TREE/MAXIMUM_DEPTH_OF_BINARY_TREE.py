# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height=0
        curr=0
        def postorder(node):
            nonlocal height
            nonlocal curr
            if not node:
                height=max(height,curr)
                
                return
            curr+=1
            postorder(node.left)
            
            postorder(node.right)
            curr-=1
            
        postorder(root)
        return height
