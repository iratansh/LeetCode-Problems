class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        
        count = Counter(hand) 
        min_heap = list(count.keys()) 
        heapq.heapify(min_heap) 
        
        while min_heap:
            first = min_heap[0]  # Get the smallest number
            for i in range(groupSize):
                if count[first + i] == 0: 
                    return False
                count[first + i] -= 1  # Use one occurrence of the number
                if count[first + i] == 0:
                    if first + i != min_heap[0]:  # Check if heap order is broken
                        return False
                    heapq.heappop(min_heap)  
        
        return True
