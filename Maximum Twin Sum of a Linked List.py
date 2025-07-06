# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find mid of linked list and reverse the second half
        # p1 = first el in list1, p2 = first el in list2
        # comput twin based on p1.val + p2.val
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None

        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        p1 = prev # curr is now equal to the start of the reversed second half
        p2 = head
        maxSum = 0
        while p1:
            maxSum = max(maxSum, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return maxSum
