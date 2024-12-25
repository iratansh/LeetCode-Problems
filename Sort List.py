# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(head):
            fast = head
            slow = head

            while fast and fast.next:
                fast = fast.next.next
                if fast:
                    slow = slow.next

            second = slow.next # set second to slow.next (represents half the list)
            slow.next = None 

            return second

        def merge(first, second):
            if not first:
                return second
            
            if not second:
                return first

            if first.val < second.val: # if the value of first < the value of second
                first.next = merge(first.next, second) # set the next of first to the merged array of first and second
                return first
            else: # if the value of first > the value of second
                second.next = merge(first, second.next)
                return second

        def merge_sort(head):
            if not head or not head.next:
                return head

            second = split(head) # set second partition 
            head = merge_sort(head) # set head to sorted head
            second = merge_sort(second) # set second to sorted second partition
            return merge(head, second) # return the combined sorted linked list

        return merge_sort(head)       
    
