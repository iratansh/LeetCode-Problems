class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Step 1: Sort both lists to ensure optimal pairing.
        seats.sort()
        students.sort()
        
        # Step 2: Initialize total moves
        total_moves = 0
        
        # Step 3: Iterate through the sorted lists and sum the absolute differences.
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
            
        return total_moves
