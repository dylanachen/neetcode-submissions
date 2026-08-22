# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # for every group of k nodes we want to reverse, we need to know the node prior the first node (group_prev) and the node following the kth node (group_next)
        # we can use a helper function to find the kth node, if it does not exist, we can break from the loop and return our result from dummy.next
        # determine group_next and prev from the kth node next
        # curr is the next of the group_prev node
        # reverse the linked list as usual
        # after reversing, group_prev still points at what was originally the first node in the segment, but is now the last node after reversing
        # set temp to this now-last node of the segment, set the next pointer of the group_prev node to kth (our now-first node), and then reassign group_prev to the now-last node
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
        
            group_next = kth.next

            prev = kth.next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr