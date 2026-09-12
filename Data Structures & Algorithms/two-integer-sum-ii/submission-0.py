class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array is already sorted in non-decreasing order
        # we can use two pointers
        l = 0
        r = len(numbers) - 1

        while (l < r): 
            # if numbers[r] cant be combined with the smallest number, 
            # it cant be used in any pairs, so skip it
            if (numbers[l] + numbers[r] > target):
                r -= 1
            # if our pair is too small, increase the left index to find
            # a bigger number
            elif (numbers[l] + numbers[r] < target):
                l += 1
            else:
                return [l+1,r+1]
            