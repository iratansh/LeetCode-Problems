class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head:
            dummy = ListNode()
            dummy.next = head
            A = B = dummy

            for _ in range(n + 1):
                A = A.next
            
            while A:
                B = B.next
                A = A.next
            
            B.next = B.next.next 
            return dummy.next
        return -1
