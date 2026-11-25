#Kadane's Algoritham 
class Solution(object):
    def maxSubArray(self, nums):

        # Initialize both variables with first element
        current_sum = nums[0]
        max_sum = nums[0]

        # Start loop from index 1
        for i in range(1, len(nums)):

            # Choose between starting a new subarray
            # or continuing the previou subarray
            current_sum = max(nums[i], current_sum + nums[i])

            # Update maximum sum if current sum is greater
            max_sum = max(max_sum, current_sum)

        # Return the maximum subarray sum
        return max_sum
