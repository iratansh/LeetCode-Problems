class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        def backtrack():
            res = 0
            for tile in count:
                if count[tile] > 0:
                    count[tile] -= 1
                    res += 1
                    res += backtrack()
                    count[tile] += 1
            return res

        return backtrack()
