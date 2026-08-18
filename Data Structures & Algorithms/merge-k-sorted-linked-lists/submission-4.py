# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # Define a function to merge two lists
        # Then iteratively merge each list (i) with the next list (i+1) until all lists are combined
        # Improvement, instead of iteratively merging every list, we can merge every distinct pair of lists in rounds until one remains to perform log(k) instead of k merges
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge_lists(list1, list2))
            lists = merged_lists
        return lists[0]

    def merge_lists(self, list1, list2):
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