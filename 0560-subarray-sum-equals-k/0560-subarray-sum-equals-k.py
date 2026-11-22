class Solution(object):
    def subarraySum(self, nums, k): # k= window_size 

        count = 0   # count Subarray
        prefix_sum = 0  # Current Sum 

        freq = {0:1} # initially o sum ki frequency 1

        for num in nums:     # go each element
            prefix_sum += num    # Add num in Current Prefix_sum 

            remaining = prefix_sum - k  # Required previous prefix sum

            if remaining in freq :      # Check remaining present in  dictionary yes or no?
                count += freq[remaining]           # add frequncy

            freq[prefix_sum] = freq.get(prefix_sum, 0) +1   # Frequency update

        return count   # rerurn total subaaray




        