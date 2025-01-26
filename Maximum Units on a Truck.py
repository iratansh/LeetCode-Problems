class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnits = 0 # keeps track of total number of units loaded
        size = 0 # keeps track of how many boxes have been loaded

        for b in boxTypes:
            if size + b[0] > truckSize:  
                totalUnits += b[1] * (truckSize - size) # load as many of the highest unit boxes first
                break
            else:
                totalUnits += b[0] * b[1]
                size += b[0]
        return totalUnits
