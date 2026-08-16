# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can use a fast and slow pointer to determine if there is ever a cycle since a cycle will inevitably cause the fast and slow pointers to meet (at effictively no more time than o(n))
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        while slow and fast:
            if slow:
                slow = slow.next
            else:
                break
            if fast and fast.next:
                fast = fast.next.next
            else:
                break

            if slow == fast:
                return True
        
        return False