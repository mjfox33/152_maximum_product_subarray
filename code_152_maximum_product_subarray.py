class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        if n < 2:
            return 0
        max_product = 0
        for i in range(n-1):
            product = nums[i] * nums[i+1]
            if product > max_product:
                max_product = product
        return max_product

# this needs work as i misunderstood the question
# the subarray can be len(nums) or 1 digit