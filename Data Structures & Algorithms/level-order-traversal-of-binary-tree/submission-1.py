# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we can recursively add all the levels to their own respective lists by using BFS
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        result = []

        while q:
            layer = []
            for _ in range(len(q)):
                node = q.popleft()
                
                layer.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(layer)
        
        return result