class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            ptr = (low + high) // 2
            if (nums[ptr] > target):
                high = ptr - 1
            elif (nums[ptr] < target):
                low = ptr + 1
            else:
                return ptr

        return -1