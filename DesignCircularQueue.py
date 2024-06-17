class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            cur = ListNode(value, self.right, self.right.prev)
            self.right.prev.next = cur
            self.right.prev = cur
            self.capacity -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.capacity += 1
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        
    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.capacity == 0
