# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use BFS to traverse the tree layer by layer (FIFO queue)
        # start with a deque containing the root node
        # for each layer, we will iterate for the len of the queue
        # pop the left node, append its children to the queue, and increment the depth
        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        depth = 0

        # we start with depth=0 since we increment the count of the first level too
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1
        
        return depth