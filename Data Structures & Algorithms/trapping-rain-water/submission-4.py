class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer solution
        l = 0
        r = len(height)-1

        total_water = 0
        # track the heights of the left bar and right bar for tracking water
        leftMax = height[l]
        rightMax = height[r]
        
        while (l < r):
            # move the pointer if the left is shorter
            if (leftMax < rightMax):
                l += 1
                leftMax = max(leftMax, height[l])
                # uses the height of the left bar to add water
                total_water += leftMax - height[l]
            # right is shorter
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                # uses the height of the right bar to add water
                total_water += rightMax - height[r]
        
        return total_water
