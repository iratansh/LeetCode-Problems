"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # basically iterate through the list and check each child node 
        # CASE 1: Child node doesn't point to a linked list - continue iterating over the current linked list
        # CASE 2: Child node has a pointer to another list - start iterating that list before returning to the current list
        def flatten(node):
            curr = node
            last = node 
            while curr:
                next_node = curr.next  # Save the next pointer in advance

                # Case 1: If current node has a child, flatten the child list
                if curr.child:
                    child_head = curr.child
                    child_tail = flatten(child_head)

                    # Stitch the child list into the main list
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None  # Clear the child pointer

                    # Connect the child's tail to the next_node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    last = child_tail  # Update last to the end of the flattened child list
                    curr = next_node  # Continue from the original next node
                else:
                    last = curr
                    curr = curr.next

            return last  # Return the tail node of the flattened list

        flatten(head)
        return head
