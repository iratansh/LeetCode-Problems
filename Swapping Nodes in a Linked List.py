# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iterate once to find the length of the linked list n, and the kth node from the start 
        # then in the next iteration, the second node to swap is at index (n - k + 1)
        # in the same iteration, swap both node values
        curr = head
        kth = None
        N = 0
        it = 0
        while curr:
            if it == (k - 1):
                kth = curr
            
            it += 1
            N += 1
            curr = curr.next
        
        curr = head
        it = 0
        while curr:
            if it == (N - k):
                kth.val, curr.val = curr.val, kth.val
                break
            it += 1
            curr = curr.next
            

        return head
