class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, path):
            if sum(path) == target:
                res.append(path.copy())
            
            if sum(path) > target or i > len(candidates):
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                backtrack(j, path)
                path.pop()
        
        res = []
        backtrack(0, [])
        return res
