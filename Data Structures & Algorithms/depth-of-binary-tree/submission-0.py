# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we can use iterative DFS (pre-ordered)
        # using a stack with LIFO, add the root node paired with its depth
        # pop the end of the stack (LI) and if it exists, update max_depth (if appropriate) and add its children nodes along with depth+1
        # return the max_depth found
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return max_depth