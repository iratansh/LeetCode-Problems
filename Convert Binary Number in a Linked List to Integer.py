# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # store the representation of the binary to a string
        # convert string to decimal
        binary = ""
        curr = head
        while curr:
            binary += str(curr.val)
            curr = curr.next


        return int(binary, 2)
