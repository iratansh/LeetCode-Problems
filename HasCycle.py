class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p, fast_p = head, head
        while fast_p and fast_p.next != None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False
