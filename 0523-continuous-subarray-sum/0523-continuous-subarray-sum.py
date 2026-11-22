
class Solution(object):
    def checkSubarraySum(self, nums, k):

        prefix_sum = 0

        freq = {0: -1}               # Store frequency and its first index

        for i in range(len(nums)):
            prefix_sum += nums[i]           # Calculate prefix sum

            remainder = prefix_sum % k     # Calculate remainder

            if remainder in freq:             # Check if remainder already exists
                length = i - freq[remainder]  # Calculate subarray length
                
                if length >= 2:     # Subarray length must be at least 2
                    return True

            else:
                freq[remainder] = i   # Store only the first occurrence

        return False
