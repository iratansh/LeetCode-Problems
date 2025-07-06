class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        arr = []
        while nums:
            alice = heappop(nums)
            bob = heappop(nums)
            arr.append(bob)
            arr.append(alice)
        return arr
