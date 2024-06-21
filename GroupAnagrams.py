class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for el in string:
                count[ord(el) - ord("a")] += 1
            
            res[tuple(count)].append(string)
        return res.values()
