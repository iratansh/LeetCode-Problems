class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            second = slow.next
            slow.next = None
            prev = None
            while second:
                temp = second.next
                second.next = prev
                prev = second
                second = temp

            first, second = head, prev
            while second:
                tmp1, tmp2 = first.next, second.next
                first.next = second
                second.next = tmp1
                first, second = tmp1, tmp2
