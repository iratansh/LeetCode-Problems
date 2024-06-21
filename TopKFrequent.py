class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count_dict = {}
        
        for el in nums:
            if el not in count_dict:
                count_dict[el] = 0
        for el in nums:
            count_dict[el] += 1
        sorted_by_values = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
        res = {i: sorted_by_values[i] for i in list(sorted_by_values)[:k]}
        res = res.keys()        
        return res
