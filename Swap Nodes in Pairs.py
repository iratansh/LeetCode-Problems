class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  
        curr = head  
        
        while curr and curr.next:
            first = curr
            second = curr.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            curr = first.next
        
        return dummy.next
