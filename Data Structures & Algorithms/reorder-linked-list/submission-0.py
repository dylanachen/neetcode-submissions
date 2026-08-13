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

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the second half of the linked list
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
        head = tail = ListNode()

        while left:
            left_temp = left.next

            tail.next = left
            left = left.next
            tail = tail.next

            if right is None:
                break
            right_temp = right.next
            tail.next = right
            right = right.next
            tail = tail.next
        
        # return head.next