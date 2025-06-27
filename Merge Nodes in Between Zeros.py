# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # basically just sum the values of the nodes starting from the starting 0 ending at the ending 0
        # the ending 0 becomes the next windows starting 0
        curr = head.next
        win_sum = 0 
        dummy = ListNode()
        curr2 = dummy
    
        while curr:
            if curr.val != 0:
                win_sum += curr.val
            if curr.val == 0:
                curr2.next = ListNode(val=win_sum)
                curr2 = curr2.next
                win_sum = 0
            curr = curr.next
            
        return dummy.next
