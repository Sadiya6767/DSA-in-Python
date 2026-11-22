
class Solution(object):
    def minSubArrayLen(self, target, nums):

        left = 0
        current_sum = 0

        min_length = float('inf')
        
        for right in range(len(nums)):

            # Add current element
            current_sum += nums[right]

            # Shrink window while target is reached
            while current_sum >= target:

                # Calculate minimum length
                min_length = min(
                    min_length,
                    right - left + 1
                )

                # Remove left element
                current_sum -= nums[left]

                left += 1

        # If no valid subarray exists
        if min_length == float('inf'):
            return 0

        return min_length
