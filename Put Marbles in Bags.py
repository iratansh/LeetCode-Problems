class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairwise_sums = [0] * (len(weights) - 1)
        for i in range(len(weights) - 1):
            pairwise_sums[i] = weights[i] + weights[i+1]
        minHeap = pairwise_sums
        maxHeap = [-num for num in pairwise_sums]
        heapify(minHeap)
        heapify(maxHeap)

        max_total = 0
        min_total = 0
        for _ in range(k - 1):
            num1 = -1 * heappop(maxHeap)
            max_total += num1
            num2 = heappop(minHeap)
            min_total += num2

        return max_total - min_total
