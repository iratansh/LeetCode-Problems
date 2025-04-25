# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # mid = ceil(n / 2)
        # set the first pointers speed to 1 and the second pointers speed to 2
        # when the second pointer reaches the end of the array, that means we break out of the loop
        # slow should now be equal to the node to be deleted
        if not head or not head.next:
            return None
        curr = head

        slow, fast = curr, curr
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        before_slow = curr
        while before_slow.next != slow:
            before_slow = before_slow.next

        before_slow.next = before_slow.next.next
        
        return curr 
