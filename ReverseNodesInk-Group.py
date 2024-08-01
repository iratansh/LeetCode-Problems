class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head
        
        prev, curr = None, head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = self.reverseKGroup(curr, k)
        return prev
