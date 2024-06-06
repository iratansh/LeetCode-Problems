class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while dummy and dummy.next != None:
            if dummy.next.val == dummy.val:
                dummy.next = dummy.next.next
                continue
            dummy = dummy.next
        return head
