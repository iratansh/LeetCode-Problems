class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
