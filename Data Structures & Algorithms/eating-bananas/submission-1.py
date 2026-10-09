import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        result = high

        while low <= high:
            k = (low + high) // 2

            # calculate how many hours it takes at this k value
            hours = sum(math.ceil(pile / k) for pile in piles)
            if hours <= h:
                result = k
                high = k - 1
            else:
                low = k + 1
        
        return result