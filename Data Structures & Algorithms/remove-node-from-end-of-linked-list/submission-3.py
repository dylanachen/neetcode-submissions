# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a pointer and a delayed pointer that we only set off after the first pointer has traversed n nodes
        # By the time the pointer has reached the end (pointer.next == None), the delayed pointer will be n from the end
        # If f.next == None, re-point the curr to next.next before moving the delayed pointer at all
        if head.next == None:
            return ListNode(val="")
        
        dummy = ListNode()
        dummy.next = head
        pointer = dummy
        delayed = dummy

        for _ in range(n):
            print(pointer.val, pointer.next.val)
            pointer = pointer.next

        while pointer.next:            
            print(pointer.val, pointer.next.val, delayed.val, delayed.next.val)
            pointer = pointer.next
            delayed = delayed.next
        
        delayed.next = delayed.next.next

        return dummy.next