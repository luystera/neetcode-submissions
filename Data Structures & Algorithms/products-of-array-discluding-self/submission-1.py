class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1] * len(nums)
        # calculate the prefix products
        prefix = 1
        for i in range(len(nums)):
            product_array[i] *= prefix
            prefix *= nums[i]
        # calculate the suffix products
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            product_array[i] *= suffix
            suffix *= nums[i]
        return product_array