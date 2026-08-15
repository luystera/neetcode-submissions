class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1] * len(nums)
        # calculate the prefix products, starting at 1
        for i in range(1, len(nums)):
            product_array[i] = product_array[i-1] * nums[i-1]
        # calculate the suffix products
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            product_array[i] *= suffix
            suffix *= nums[i]
        return product_array