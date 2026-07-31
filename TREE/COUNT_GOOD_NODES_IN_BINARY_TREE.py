# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        good=0
        def max_value(node,maxvalue):
            nonlocal good
            if not node:
                return
            if node.val>=maxvalue:
                good+=1
                maxvalue=max(node.val,maxvalue)
            max_value(node.left,maxvalue)
            max_value(node.right,maxvalue)
        max_value(root,root.val)
        return good


        