# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use head to store a reference to the beginning of the new linked list we are making
        # tail is an additional pointer we will use to construct the output in place
        # while neither of the list pointers are None, compare their values
        # if list1.val is smaller, make our tail pointers next point to list1, advancing our list1 pointer to its next node (same goes if list2.val is smaller)
        # advance our tail pointer to its next node
        # the loop will break once one of the lists reaches its end (pointer becomes None)
        # in that case, point our last node at the remainder of the other still-existing list
        # return the head of our list from the head node created earlier

        head = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2

        return head.next