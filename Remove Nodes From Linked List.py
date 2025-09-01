# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse linked list, keep track of max value seen so far
        # compare current value with that value
        curr = head
        head2 = curr
        prev = None

        maxVal = 0
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        
        dummy = ListNode(0)
        tail = dummy
        maxVal = float('-inf')
        curr = prev
        while curr:
            if curr.val >= maxVal:
                maxVal = curr.val
                tail.next = curr
                tail = tail.next
            curr = curr.next
        tail.next = None

        prev, curr = None, dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
