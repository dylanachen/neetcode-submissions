# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a head node that starts our result (curr) and initial carry of 0
        # while a number list or our carry-over exists, get their values and find the digit sum
        # calculate the carry from the digit sum and mod 10 to get the ones digit
        # create the next node with the ones digit and advance the result
        # advance the number lists if they exist
        head = ListNode()
        curr = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digit_sum = val1 + val2 + carry
            carry = digit_sum // 10
            digit_sum = digit_sum % 10
            curr.next = ListNode(digit_sum)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next