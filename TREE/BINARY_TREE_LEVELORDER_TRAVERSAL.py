# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        result = []
        # Double-ended queue (deque) use kar rahe hain efficient popleft() ke liye
        queue = deque([root])
        
        while queue:
            # Front node ko nikalein
            
            curr=[]
            
            lenq=len(queue)
            
            for i in range(lenq):
                currNode=queue.popleft()
                curr.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                
                # Phir right child ko queue mein daalein
                if currNode.right:
                    queue.append(currNode.right)
            result.append(curr)
            # Pehle left child ko queue mein daalein
            
                
        return result