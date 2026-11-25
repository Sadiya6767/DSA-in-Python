class Solution(object):
    def maxProduct(self, nums):

        # Initially first element se start
        max_product = nums[0]
        min_product = nums[0]
        product = nums[0]

        for i in range(1, len(nums)):

            # Negative number hai toh max aur min swap
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            # Maximum product update
            max_product = max(nums[i], max_product * nums[i])

            # Minimum product update
            min_product = min(nums[i], min_product * nums[i])

            # Overall maximum answer update
            product = max(product, max_product)

        return product