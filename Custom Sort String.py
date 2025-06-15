class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = defaultdict(int)
        res = ""
        for i, char in enumerate(order):
            if char not in hashmap:
                hashmap[char] = i
        sorted_s = sorted(s, key=lambda c: hashmap[c] if c in hashmap else float('inf'))

        return "".join(sorted_s)
