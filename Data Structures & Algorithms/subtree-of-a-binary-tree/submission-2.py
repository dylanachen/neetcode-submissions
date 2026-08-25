# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if there is no subroot, its always true. if there is no root, it is always false
        if not subRoot:
            return True
        if not root:
            return False
        
        # for every node in the main tree, see if the same tree helper function returns True, otherwise, run on both children nodes
        if self.same_tree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
    
        # same as same_tree problem using recursive DFS
    def same_tree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.same_tree(root.left, subRoot.left)) and (self.same_tree(root.right, subRoot.right))
        return False