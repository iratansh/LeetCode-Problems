class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        freq = defaultdict(list) # key = size, val = indexes in groupSizes which have size = key

        for i, size in enumerate(groupSizes):
            if size == 1:
                groups.append([i])
            else:
                freq[size].append(i)
                if len(freq[size]) == size:
                    groups.append(freq[size])
                    freq[size] = []
        return groups
