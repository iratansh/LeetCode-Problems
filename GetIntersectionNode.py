class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        while currA != currB:
            currA  = headB if currA is None else currA.next
            currB  = headA if currB is None else currB.next
        return currA
