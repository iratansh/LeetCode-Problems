class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        numDays = len(security)
        if numDays <= time * 2:
            return []
        nonIncreasing = [0] * numDays
        nonDecreasing = [0] * numDays

        for i in range(1, numDays):
            if security[i] <= security[i - 1]:
                nonIncreasing[i] = nonIncreasing[i - 1] + 1
        
        for i in range(numDays - 2, -1, -1):
            if security[i] <= security[i + 1]:
                nonDecreasing[i] = nonDecreasing[i + 1] + 1
        
        goodDays = [i for i in range(numDays) if time <= min(nonIncreasing[i], nonDecreasing[i])]
        return goodDays
