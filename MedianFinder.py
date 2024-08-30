class MedianFinder:

    def __init__(self):
        self.smallHeap = [] # max heap
        self.largeHeap = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)

        if (self.smallHeap and self.largeHeap and (self.smallHeap[0] * -1) > self.largeHeap[0]):
            val = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.largeHeap, val)
        
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap) * -1
            heapq.heappush(self.smallHeap, val)

        
    def findMedian(self) -> float:
        # even: max value of small heap + min value of large heap / 2
        # odd: max of the small heap or min of large heap depending on which one has more values
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0]
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        return ((-1 * self.smallHeap[0]) + self.largeHeap[0]) / 2
