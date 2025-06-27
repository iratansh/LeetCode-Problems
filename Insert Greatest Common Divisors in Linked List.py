# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def computeGCD(a, b):
            while b:
                a, b = b, a % b
            return a

        dummy = ListNode()
        curr = head
        curr2 = dummy
        while curr and curr.next:
            curr2.next = curr 
            curr2 = curr2.next

            a, b = curr.val, curr.next.val
            node = ListNode(val=computeGCD(a, b))
            curr = curr.next

            curr2.next = node
            curr2 = curr2.next
        curr2.next = curr
        return dummy.next
