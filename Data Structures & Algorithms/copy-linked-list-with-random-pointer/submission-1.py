"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # traverse the linked list start to finish, creating a new node for each node in the input linked list
        # simultaneously create a dict of original_node: copy_node
        # perform a second pass of the original linked list and use the next and random pointers to lookup in the dict to assign the next and random copy node pointers
        pass1 = head
        pass2 = head
        node_map = {}

        while pass1:
            copy_node = Node(pass1.val)
            node_map[pass1] = copy_node
            pass1 = pass1.next
        
        while pass2:
            copy_node = node_map[pass2]
            copy_node.next = node_map.get(pass2.next)
            copy_node.random = node_map.get(pass2.random)
            pass2 = pass2.next
        
        return node_map.get(head)