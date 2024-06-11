class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head
            prev = None

            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            head = prev
            return head
        return 
