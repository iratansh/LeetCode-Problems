class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        dummy = []
        for key, val in freq.items():
            dummy.append((-val, key))
        heapify(dummy)
        res = []
        while dummy:
            val, key = heappop(dummy)
            for _ in range(val * -1):
                res.append(key)
        return "".join(res)
