# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # a valid BST is a binary tree such that each node has a left subtree less than its value and a right subtree that is greater than it
        # we can perform recursive DFS feeding the current node along with the current left and right bounds (which start and -/+ infinity)
        # if the node doesn't exist, return True
        # if the node value does not fall within the range, return False
        # return the DFS of the left child, setting the new right bound as the current node, and the DFS of the right child with the updated left bound
        def valid(node, left_bound, right_bound):
            if not node:
                return True

            if not (left_bound < node.val < right_bound):
                return False
            
            return valid(node.left, left_bound, node.val) and valid(node.right, node.val, right_bound)
        
        return valid(root, float('-inf'), float('inf'))