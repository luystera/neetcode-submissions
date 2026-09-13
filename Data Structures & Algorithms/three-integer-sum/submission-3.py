class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first
        nums.sort()
        ret_arr = []

        for i in range(len(nums)):
            # skip duplicate values
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            # 3 positive numbers can't sum to zero
            if (nums[i] > 0):
                break
            # use two pointers
            l = i + 1 # search to the right of index i
            r = len(nums) - 1
            # then use 2sum approach
            while (l < r):
                if (nums[l] + nums[r] < -nums[i]):
                    l += 1
                elif (nums[l] + nums[r] > -nums[i]):
                    r -= 1
                else:
                    ret_arr.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
        
        return ret_arr