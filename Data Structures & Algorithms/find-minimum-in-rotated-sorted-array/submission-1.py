class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = (low + high) // 2
            if (nums[mid] > nums[high]):
                # the minimum exists to the right
                # need to move to the right half of the array
                low = mid + 1
            else:
                # the minimum is either mid or to the left of mid
                # need to move to the left but dont want to skip nums[mid]
                high = mid
        
        return nums[low]