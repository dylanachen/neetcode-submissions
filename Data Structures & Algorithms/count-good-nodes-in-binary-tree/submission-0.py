# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive DFS where we track the max value seen in the path so far
        if not root:
            return 0
        max_seen = root.val

        def dfs(node, max_seen):
            if not node:
                return 0

            if node.val >= max_seen:
                max_seen = node.val
                res = 1
            else:
                res = 0
            res += dfs(node.left, max_seen)
            res += dfs(node.right, max_seen)

            return res
        
        num_good = dfs(root, max_seen)

        return num_good