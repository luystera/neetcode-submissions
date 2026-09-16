class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer solution
        l = 0
        r = len(heights)-1
        max_amt = 0

        while (l < r):
            # calculate the amount of water at these indices
            water = (r - l) * min(heights[l], heights[r])
            # greedy approach, keep the index with taller height
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
            # update maximum amount of water seen so far
            if (water > max_amt):
                max_amt = water
        
        return max_amt

