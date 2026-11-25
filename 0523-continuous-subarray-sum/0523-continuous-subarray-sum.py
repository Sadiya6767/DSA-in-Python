
class Solution:
    def checkSubarraySum(self, nums, k):

        # Store remainder and its first index
        remainder_map = {0: -1}

        prefix_sum = 0

        for i in range(len(nums)):

            # Calculate prefix sum
            prefix_sum += nums[i]

            # Calculate remainder
            remainder = prefix_sum % k

            # Check if remainder already exists
            if remainder in remainder_map:

                # Check subarray length >= 2
                if i - remainder_map[remainder] >= 2:
                    return True

            else:
                # Store remainder with its index
                remainder_map[remainder] = i

        return False
