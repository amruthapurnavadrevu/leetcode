from typing import List

class Solution: 
    def ClosestToZero(self, nums: List[int]) -> int:
        potential_values = []
        m = min(abs(i) for i in nums)
        
        for i in nums:
            if abs(i) == m:
                potential_values.append(i)
        
        if len(potential_values) > 0:
            return max(potential_values)
        else:
            return m

