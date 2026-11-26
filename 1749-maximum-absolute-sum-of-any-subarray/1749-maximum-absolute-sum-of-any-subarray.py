
class Solution(object):
    def maxAbsoluteSum(self, nums):

        # Initialize variables
        current_max = 0
        max_sum = 0

        current_min = 0
        min_sum = 0

        # Traverse the array
        for num in nums:

            # Find maximum subarray sum
            current_max = max(0, current_max + num)
            max_sum = max(max_sum, current_max)

            # Find minimum subarray sum
            current_min = min(0, current_min + num)
            min_sum = min(min_sum, current_min)

        # Compare positive and negative maximum sums
        return max(max_sum, abs(min_sum))
