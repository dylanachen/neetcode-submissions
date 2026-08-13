# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Slow and fast pointers to locate the middle of the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the second half of the linked list (starting with the first node of the second half, not the last node of the first half)
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Constructing re-ordered linked list
        left = head
        right = prev

        while right:
            left_temp = left.next
            right_temp = right.next

            left.next = right
            right.next = left_temp

            left = left_temp
            right = right_temp