class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = {None: None}
        curr = head

        while curr:
            copy = Node(curr.val)
            old[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = old[curr]  
            copy.next = old[curr.next]
            copy.random = old[curr.random]
            curr = curr.next
        
        return old[head]
