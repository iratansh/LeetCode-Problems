# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # set a-1.next to list2, set list2.next to b + 1
        curr1 = list1
        curr2 = list1
        curr_indexA, curr_indexB = 0, 0
        while curr_indexA < a - 1: # iterate until we reach the a-1 th node
            curr1 = curr1.next
            curr_indexA += 1
        while curr_indexB < b + 1: # iterate until we reach b+1th node
            curr2 = curr2.next
            curr_indexB += 1
        curr1.next = list2 
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        
        tail2.next = curr2
        return list1



