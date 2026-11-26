class Solution(object):
    def maxSubarraySumCircular(self, nums):
        
        # Initialize variables
        total_sum = 0
        
        # maximum
        current_max = 0
        max_sum = float('-inf')
        
        # minimum
        current_min = 0
        min_sum = float('inf')
        
        # Traverse the array
        for num in nums:
            
            total_sum += num    

            # Kadane's Algorithm for maximum subarray
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            

            # Kadane's Algorithm for minimum subarray
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
        
        # If all elements are negative,
        # circular case should not be considered
        if max_sum < 0:
            return max_sum
        
        # Maximum circular sum = total sum - minimum subarray
        circular_sum = total_sum - min_sum
        
        # Return the maximum of both cases
        return max(max_sum, circular_sum)

        