class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(i, path):
            if sum(path) == target:
                res.append(path.copy())

            if i > len(candidates) or sum(path) > target:
                return
            
            for j in range(i, len(candidates)):
                if j != i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                backtrack(j + 1, path)
                path.pop()
        
        res = []
        backtrack(0, [])
        return res
