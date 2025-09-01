class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for el in operations:
            operator = el[:2] if "X" not in el[:2] else el[1::]
            if operator == "++":
                res += 1
            else:
                res -= 1
        return res
