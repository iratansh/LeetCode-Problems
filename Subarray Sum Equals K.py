class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        curr_sum = 0
        count = 0

        for el in nums:
            curr_sum += el
            if curr_sum - k in freq:
                count += freq[curr_sum - k]
            freq[curr_sum] += 1
        return count
