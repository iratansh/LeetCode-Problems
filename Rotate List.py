class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        k = k % length  
        steps_to_new_head = length - k
        
        curr = head
        for _ in range(steps_to_new_head - 1):
            curr = curr.next
        
        new_head = curr.next
        curr.next = None
        
        return new_head
