# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative BFS, but only add the very last entry of each len(q) loop to the result list and do not append nulls to the queue
        if not root:
            return []
        
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                
                if i == q_len - 1:
                    result.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return result