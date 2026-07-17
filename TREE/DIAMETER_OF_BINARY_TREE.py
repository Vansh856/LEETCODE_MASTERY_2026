# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia=0
        def get_hight(node):
            nonlocal max_dia
            if not node:
                return 0
            left=get_hight(node.left)
            right=get_hight(node.right)
            max_dia=max(max_dia,left+right)
            return max(left,right)+1

        get_hight(root)
        return max_dia
            