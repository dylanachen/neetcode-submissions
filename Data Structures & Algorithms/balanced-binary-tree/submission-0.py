# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we can use recusrive DFS to compare the heights of the subtrees of each node
        # if the difference > 1, return False, otherwise return True
        if not root:
            return True

        balanced = True

        def dfs(root):
            nonlocal balanced

            if not root:
                return 0
                
            left = dfs(root.left)
            right = dfs(root.right)
            
            difference = abs(right - left)
            if difference > 1:
                balanced = False

            return 1 + max(left, right)

        dfs(root)
        
        return balanced