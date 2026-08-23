# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative DFS using a stack of paired nodes from left and right
        stack = [(p, q)]

        # traverse whole tree
        while stack:
            p_node, q_node = stack.pop()

            # if both are null, it is still valid, but there is no child nodes to add to the stack
            if not p_node and not q_node:
                continue
            
            # if only one is null, or they are unequal, tree is not same
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
                
            stack.append((p_node.left, q_node.left))
            stack.append((p_node.right, q_node.right))
        
        return True