class Solution:
    def subarraysDivByK(self, nums, k):

        prefix = 0       # Stores the cumulative sum
        count = 0        # Counts divisible subarrays

        freq = {0: 1}    # Initially remainder 0 occurs once

        for num in nums:                 # Traverse every array element

            prefix += num               # Add current element to prefix sum

            remainder = prefix % k      # Calculate remainder of prefix sum

            if remainder in freq:       # Check if same remainder appeared before
                count += freq[remainder] # Add its frequency to count

            freq[remainder] = freq.get(remainder, 0) + 1
            # Increase frequency of current remainder

        return count                    # Return total divisible subarrays