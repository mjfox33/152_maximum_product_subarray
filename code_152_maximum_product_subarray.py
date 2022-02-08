import math
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        if n < 2:
            return nums[0]
        prefix = 0
        suffix = 0
        max_product = -math.inf
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_product = max(max_product, prefix, suffix)
        return max_product

# this needs work as i misunderstood the question
# the subarray can be len(nums) or 1 digit