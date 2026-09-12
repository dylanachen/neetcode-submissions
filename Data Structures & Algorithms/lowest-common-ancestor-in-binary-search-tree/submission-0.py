# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # starting at the root node, if the root is > both p and q, p and q LCA be to the left
        # if root < p and q, LCA must be to the right
        # if root = p or q, root is LCA
        # if root < p and > q, root is LCA
        node = root

        while node:
            if node.val == p.val or node.val == q.val:
                return node
            if (node.val < p.val and node.val > q.val) or (node.val > p.val and node.val < q.val):
                return node
            
            if node.val < p.val and node.val < q.val:
                node = node.right
            if node.val > p.val and node.val > q.val:
                node = node.left
        