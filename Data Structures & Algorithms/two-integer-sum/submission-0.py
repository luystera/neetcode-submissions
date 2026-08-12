class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store numbers we've seen so far in the list with their index
        seen = {}
        for i,num in enumerate(nums):
            # the complement is the number that pairs with the given num
            complement = target - num
            # check if we've seen the complement yet
            if complement in seen:
                # return the indices
                return [seen[complement], i]
            # add num to hashmap
            seen[num] = i