class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left = 0
        right = 0
        product = 1
        count = 0

        if k <=1:
            return 0 

        for right in range(len(nums)):
            product = product * nums[right]

            while product >= k:
                product = product // nums[left]
                left = left + 1
           

            count = count + right - left + 1
        
        return count 