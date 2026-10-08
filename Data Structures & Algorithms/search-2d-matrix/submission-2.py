class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the row that the number would exist in
        for row in matrix:
            if target <= row[-1]:
                # binary search this row for the target
                return self.binSearch(row, target)
        return False

    def binSearch(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            ptr = (low + high) // 2
            if (nums[ptr] < target):
                low = ptr + 1
            elif (nums[ptr] > target):
                high = ptr - 1
            else:
                return True
        
        return False